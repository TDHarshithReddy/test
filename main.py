"""
Dental Mobile Application
A comprehensive dental practice management application
"""

import os
os.environ['KIVY_NO_CONSOLELOG'] = '1'

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from datetime import datetime, timedelta
import json

Window.clearcolor = (0.95, 0.95, 0.97, 1)


class DataManager:
    """Manages application data persistence"""
    
    def __init__(self):
        self.data_dir = 'data'
        self.patients_file = os.path.join(self.data_dir, 'patients.json')
        self.appointments_file = os.path.join(self.data_dir, 'appointments.json')
        self.treatments_file = os.path.join(self.data_dir, 'treatments.json')
        self._ensure_data_dir()
        
    def _ensure_data_dir(self):
        if not os.path.exists(self.data_dir):
            os.makedirs(self.data_dir)
            
    def load_data(self, filename):
        try:
            with open(filename, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}
            
    def save_data(self, filename, data):
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
    def get_patients(self):
        return self.load_data(self.patients_file)
        
    def save_patients(self, patients):
        self.save_data(self.patients_file, patients)
        
    def get_appointments(self):
        return self.load_data(self.appointments_file)
        
    def save_appointments(self, appointments):
        self.save_data(self.appointments_file, appointments)
        
    def get_treatments(self):
        return self.load_data(self.treatments_file)
        
    def save_treatments(self, treatments):
        self.save_data(self.treatments_file, treatments)


class HomeScreen(Screen):
    """Main dashboard screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'home'
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        title = Label(
            text='Dental Practice Manager',
            size_hint_y=0.15,
            font_size='28sp',
            bold=True,
            color=(0.2, 0.4, 0.7, 1)
        )
        layout.add_widget(title)
        
        stats_layout = GridLayout(cols=2, spacing=10, size_hint_y=0.2)
        
        data_mgr = DataManager()
        patients = data_mgr.get_patients()
        appointments = data_mgr.get_appointments()
        
        today = datetime.now().strftime('%Y-%m-%d')
        today_appointments = sum(1 for apt in appointments.values() if apt.get('date') == today)
        
        stats_layout.add_widget(self._create_stat_card('Total Patients', str(len(patients))))
        stats_layout.add_widget(self._create_stat_card('Today\'s Appointments', str(today_appointments)))
        
        layout.add_widget(stats_layout)
        
        menu_grid = GridLayout(cols=2, spacing=15, size_hint_y=0.65)
        
        buttons = [
            ('Patients', 'patients', (0.3, 0.6, 0.9, 1)),
            ('Appointments', 'appointments', (0.4, 0.7, 0.5, 1)),
            ('Dental Chart', 'dental_chart', (0.9, 0.5, 0.3, 1)),
            ('Treatments', 'treatments', (0.7, 0.4, 0.8, 1)),
        ]
        
        for text, screen_name, color in buttons:
            btn = Button(
                text=text,
                font_size='20sp',
                bold=True,
                background_color=color,
                background_normal=''
            )
            btn.bind(on_press=lambda x, s=screen_name: self.switch_screen(s))
            menu_grid.add_widget(btn)
            
        layout.add_widget(menu_grid)
        self.add_widget(layout)
        
    def _create_stat_card(self, title, value):
        card = BoxLayout(orientation='vertical', padding=10)
        with card.canvas.before:
            Color(1, 1, 1, 1)
            card.rect = Rectangle(pos=card.pos, size=card.size)
        card.bind(pos=self._update_rect, size=self._update_rect)
        
        card.add_widget(Label(text=value, font_size='32sp', bold=True, color=(0.2, 0.4, 0.7, 1)))
        card.add_widget(Label(text=title, font_size='14sp', color=(0.5, 0.5, 0.5, 1)))
        return card
        
    def _update_rect(self, instance, value):
        instance.rect.pos = instance.pos
        instance.rect.size = instance.size
        
    def switch_screen(self, screen_name):
        self.manager.current = screen_name


class PatientsScreen(Screen):
    """Patient management screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'patients'
        self.data_mgr = DataManager()
        self.build_ui()
        
    def build_ui(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header = BoxLayout(size_hint_y=0.1, spacing=10)
        back_btn = Button(text='← Back', size_hint_x=0.3, background_color=(0.5, 0.5, 0.5, 1))
        back_btn.bind(on_press=lambda x: self.go_back())
        header.add_widget(back_btn)
        
        title = Label(text='Patients', font_size='24sp', bold=True, size_hint_x=0.4)
        header.add_widget(title)
        
        add_btn = Button(text='+ Add Patient', size_hint_x=0.3, background_color=(0.3, 0.7, 0.3, 1))
        add_btn.bind(on_press=lambda x: self.show_add_patient_dialog())
        header.add_widget(add_btn)
        
        layout.add_widget(header)
        
        scroll = ScrollView(size_hint=(1, 0.9))
        self.patient_list = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        self.patient_list.bind(minimum_height=self.patient_list.setter('height'))
        
        patients = self.data_mgr.get_patients()
        for patient_id, patient in patients.items():
            self.add_patient_item(patient_id, patient)
            
        scroll.add_widget(self.patient_list)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
        
    def add_patient_item(self, patient_id, patient):
        item = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, padding=10, spacing=10)
        
        with item.canvas.before:
            Color(1, 1, 1, 1)
            item.rect = Rectangle(pos=item.pos, size=item.size)
        item.bind(pos=lambda i, v: setattr(i.rect, 'pos', v), 
                 size=lambda i, v: setattr(i.rect, 'size', v))
        
        info = BoxLayout(orientation='vertical', size_hint_x=0.7)
        info.add_widget(Label(text=patient['name'], font_size='18sp', bold=True, halign='left'))
        info.add_widget(Label(text=f"Phone: {patient['phone']}", font_size='14sp', halign='left'))
        
        view_btn = Button(text='View', size_hint_x=0.3, background_color=(0.3, 0.6, 0.9, 1))
        view_btn.bind(on_press=lambda x, pid=patient_id: self.view_patient(pid))
        
        item.add_widget(info)
        item.add_widget(view_btn)
        self.patient_list.add_widget(item)
        
    def show_add_patient_dialog(self):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        content.add_widget(Label(text='Patient Name:', size_hint_y=None, height=30))
        name_input = TextInput(multiline=False, size_hint_y=None, height=40)
        content.add_widget(name_input)
        
        content.add_widget(Label(text='Phone:', size_hint_y=None, height=30))
        phone_input = TextInput(multiline=False, size_hint_y=None, height=40)
        content.add_widget(phone_input)
        
        content.add_widget(Label(text='Email:', size_hint_y=None, height=30))
        email_input = TextInput(multiline=False, size_hint_y=None, height=40)
        content.add_widget(email_input)
        
        content.add_widget(Label(text='Date of Birth:', size_hint_y=None, height=30))
        dob_input = TextInput(multiline=False, size_hint_y=None, height=40, hint_text='YYYY-MM-DD')
        content.add_widget(dob_input)
        
        buttons = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        popup = Popup(title='Add New Patient', content=content, size_hint=(0.9, 0.7))
        
        save_btn = Button(text='Save', background_color=(0.3, 0.7, 0.3, 1))
        save_btn.bind(on_press=lambda x: self.save_patient(
            name_input.text, phone_input.text, email_input.text, dob_input.text, popup))
        buttons.add_widget(save_btn)
        
        cancel_btn = Button(text='Cancel', background_color=(0.7, 0.3, 0.3, 1))
        cancel_btn.bind(on_press=popup.dismiss)
        buttons.add_widget(cancel_btn)
        
        content.add_widget(buttons)
        popup.open()
        
    def save_patient(self, name, phone, email, dob, popup):
        if not name or not phone:
            return
            
        patients = self.data_mgr.get_patients()
        patient_id = f"P{len(patients) + 1:04d}"
        
        patients[patient_id] = {
            'name': name,
            'phone': phone,
            'email': email,
            'dob': dob,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.data_mgr.save_patients(patients)
        popup.dismiss()
        self.build_ui()
        
    def view_patient(self, patient_id):
        patients = self.data_mgr.get_patients()
        patient = patients.get(patient_id)
        
        if patient:
            content = BoxLayout(orientation='vertical', spacing=10, padding=20)
            content.add_widget(Label(text=f"ID: {patient_id}", font_size='16sp'))
            content.add_widget(Label(text=f"Name: {patient['name']}", font_size='18sp', bold=True))
            content.add_widget(Label(text=f"Phone: {patient['phone']}", font_size='16sp'))
            content.add_widget(Label(text=f"Email: {patient.get('email', 'N/A')}", font_size='16sp'))
            content.add_widget(Label(text=f"DOB: {patient.get('dob', 'N/A')}", font_size='16sp'))
            
            close_btn = Button(text='Close', size_hint_y=None, height=50)
            popup = Popup(title='Patient Details', content=content, size_hint=(0.8, 0.6))
            close_btn.bind(on_press=popup.dismiss)
            content.add_widget(close_btn)
            popup.open()
            
    def go_back(self):
        self.manager.current = 'home'


class AppointmentsScreen(Screen):
    """Appointment scheduling screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'appointments'
        self.data_mgr = DataManager()
        self.build_ui()
        
    def build_ui(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header = BoxLayout(size_hint_y=0.1, spacing=10)
        back_btn = Button(text='← Back', size_hint_x=0.3, background_color=(0.5, 0.5, 0.5, 1))
        back_btn.bind(on_press=lambda x: self.go_back())
        header.add_widget(back_btn)
        
        title = Label(text='Appointments', font_size='24sp', bold=True, size_hint_x=0.4)
        header.add_widget(title)
        
        add_btn = Button(text='+ Schedule', size_hint_x=0.3, background_color=(0.4, 0.7, 0.5, 1))
        add_btn.bind(on_press=lambda x: self.show_schedule_dialog())
        header.add_widget(add_btn)
        
        layout.add_widget(header)
        
        scroll = ScrollView(size_hint=(1, 0.9))
        self.appointment_list = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        self.appointment_list.bind(minimum_height=self.appointment_list.setter('height'))
        
        appointments = self.data_mgr.get_appointments()
        sorted_appointments = sorted(appointments.items(), 
                                     key=lambda x: (x[1].get('date', ''), x[1].get('time', '')))
        
        for apt_id, apt in sorted_appointments:
            self.add_appointment_item(apt_id, apt)
            
        scroll.add_widget(self.appointment_list)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
        
    def add_appointment_item(self, apt_id, apt):
        item = BoxLayout(orientation='horizontal', size_hint_y=None, height=90, padding=10, spacing=10)
        
        with item.canvas.before:
            Color(1, 1, 1, 1)
            item.rect = Rectangle(pos=item.pos, size=item.size)
        item.bind(pos=lambda i, v: setattr(i.rect, 'pos', v),
                 size=lambda i, v: setattr(i.rect, 'size', v))
        
        info = BoxLayout(orientation='vertical', size_hint_x=0.7)
        info.add_widget(Label(text=f"{apt['patient_name']}", font_size='18sp', bold=True, halign='left'))
        info.add_widget(Label(text=f"Date: {apt['date']}", font_size='14sp', halign='left'))
        info.add_widget(Label(text=f"Time: {apt['time']}", font_size='14sp', halign='left'))
        
        status_color = (0.3, 0.7, 0.3, 1) if apt.get('status') == 'confirmed' else (0.9, 0.6, 0.3, 1)
        status_btn = Button(
            text=apt.get('status', 'pending').capitalize(),
            size_hint_x=0.3,
            background_color=status_color
        )
        
        item.add_widget(info)
        item.add_widget(status_btn)
        self.appointment_list.add_widget(item)
        
    def show_schedule_dialog(self):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        content.add_widget(Label(text='Patient ID:', size_hint_y=None, height=30))
        patient_input = TextInput(multiline=False, size_hint_y=None, height=40, hint_text='e.g., P0001')
        content.add_widget(patient_input)
        
        content.add_widget(Label(text='Date:', size_hint_y=None, height=30))
        date_input = TextInput(multiline=False, size_hint_y=None, height=40, hint_text='YYYY-MM-DD')
        content.add_widget(date_input)
        
        content.add_widget(Label(text='Time:', size_hint_y=None, height=30))
        time_input = TextInput(multiline=False, size_hint_y=None, height=40, hint_text='HH:MM')
        content.add_widget(time_input)
        
        content.add_widget(Label(text='Reason:', size_hint_y=None, height=30))
        reason_input = TextInput(multiline=False, size_hint_y=None, height=40)
        content.add_widget(reason_input)
        
        buttons = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        popup = Popup(title='Schedule Appointment', content=content, size_hint=(0.9, 0.7))
        
        save_btn = Button(text='Schedule', background_color=(0.3, 0.7, 0.3, 1))
        save_btn.bind(on_press=lambda x: self.save_appointment(
            patient_input.text, date_input.text, time_input.text, reason_input.text, popup))
        buttons.add_widget(save_btn)
        
        cancel_btn = Button(text='Cancel', background_color=(0.7, 0.3, 0.3, 1))
        cancel_btn.bind(on_press=popup.dismiss)
        buttons.add_widget(cancel_btn)
        
        content.add_widget(buttons)
        popup.open()
        
    def save_appointment(self, patient_id, date, time, reason, popup):
        if not patient_id or not date or not time:
            return
            
        patients = self.data_mgr.get_patients()
        patient = patients.get(patient_id)
        
        if not patient:
            return
            
        appointments = self.data_mgr.get_appointments()
        apt_id = f"APT{len(appointments) + 1:04d}"
        
        appointments[apt_id] = {
            'patient_id': patient_id,
            'patient_name': patient['name'],
            'date': date,
            'time': time,
            'reason': reason,
            'status': 'pending',
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.data_mgr.save_appointments(appointments)
        popup.dismiss()
        self.build_ui()
        
    def go_back(self):
        self.manager.current = 'home'


class DentalChartScreen(Screen):
    """Dental chart visualization screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'dental_chart'
        self.build_ui()
        
    def build_ui(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header = BoxLayout(size_hint_y=0.1, spacing=10)
        back_btn = Button(text='← Back', size_hint_x=0.3, background_color=(0.5, 0.5, 0.5, 1))
        back_btn.bind(on_press=lambda x: self.go_back())
        header.add_widget(back_btn)
        
        title = Label(text='Dental Chart', font_size='24sp', bold=True)
        header.add_widget(title)
        
        layout.add_widget(header)
        
        chart_container = BoxLayout(orientation='vertical', spacing=20, padding=20)
        
        upper_teeth = GridLayout(cols=16, spacing=5, size_hint_y=0.4)
        tooth_numbers_upper = list(range(1, 17))
        
        for tooth_num in tooth_numbers_upper:
            tooth_btn = Button(
                text=str(tooth_num),
                background_color=(1, 1, 1, 1),
                color=(0, 0, 0, 1)
            )
            tooth_btn.bind(on_press=lambda x, t=tooth_num: self.show_tooth_info(t))
            upper_teeth.add_widget(tooth_btn)
            
        chart_container.add_widget(Label(text='Upper Teeth', size_hint_y=0.1, font_size='18sp'))
        chart_container.add_widget(upper_teeth)
        
        chart_container.add_widget(Label(text='━━━━━━━━━━━━━━━━', size_hint_y=0.1))
        
        lower_teeth = GridLayout(cols=16, spacing=5, size_hint_y=0.4)
        tooth_numbers_lower = list(range(17, 33))
        
        for tooth_num in tooth_numbers_lower:
            tooth_btn = Button(
                text=str(tooth_num),
                background_color=(1, 1, 1, 1),
                color=(0, 0, 0, 1)
            )
            tooth_btn.bind(on_press=lambda x, t=tooth_num: self.show_tooth_info(t))
            lower_teeth.add_widget(tooth_btn)
            
        chart_container.add_widget(Label(text='Lower Teeth', size_hint_y=0.1, font_size='18sp'))
        chart_container.add_widget(lower_teeth)
        
        layout.add_widget(chart_container)
        self.add_widget(layout)
        
    def show_tooth_info(self, tooth_number):
        content = BoxLayout(orientation='vertical', spacing=10, padding=20)
        content.add_widget(Label(text=f'Tooth #{tooth_number}', font_size='20sp', bold=True))
        content.add_widget(Label(text='Condition: Healthy', font_size='16sp'))
        content.add_widget(Label(text='Last Check: N/A', font_size='16sp'))
        
        close_btn = Button(text='Close', size_hint_y=None, height=50)
        popup = Popup(title=f'Tooth #{tooth_number} Details', content=content, size_hint=(0.7, 0.5))
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        popup.open()
        
    def go_back(self):
        self.manager.current = 'home'


class TreatmentsScreen(Screen):
    """Treatment records screen"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name = 'treatments'
        self.data_mgr = DataManager()
        self.build_ui()
        
    def build_ui(self):
        self.clear_widgets()
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        header = BoxLayout(size_hint_y=0.1, spacing=10)
        back_btn = Button(text='← Back', size_hint_x=0.3, background_color=(0.5, 0.5, 0.5, 1))
        back_btn.bind(on_press=lambda x: self.go_back())
        header.add_widget(back_btn)
        
        title = Label(text='Treatments', font_size='24sp', bold=True, size_hint_x=0.4)
        header.add_widget(title)
        
        add_btn = Button(text='+ Add Record', size_hint_x=0.3, background_color=(0.7, 0.4, 0.8, 1))
        add_btn.bind(on_press=lambda x: self.show_add_treatment_dialog())
        header.add_widget(add_btn)
        
        layout.add_widget(header)
        
        scroll = ScrollView(size_hint=(1, 0.9))
        self.treatment_list = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None)
        self.treatment_list.bind(minimum_height=self.treatment_list.setter('height'))
        
        treatments = self.data_mgr.get_treatments()
        sorted_treatments = sorted(treatments.items(), 
                                   key=lambda x: x[1].get('date', ''), 
                                   reverse=True)
        
        for treatment_id, treatment in sorted_treatments:
            self.add_treatment_item(treatment_id, treatment)
            
        scroll.add_widget(self.treatment_list)
        layout.add_widget(scroll)
        
        self.add_widget(layout)
        
    def add_treatment_item(self, treatment_id, treatment):
        item = BoxLayout(orientation='vertical', size_hint_y=None, height=100, padding=10, spacing=5)
        
        with item.canvas.before:
            Color(1, 1, 1, 1)
            item.rect = Rectangle(pos=item.pos, size=item.size)
        item.bind(pos=lambda i, v: setattr(i.rect, 'pos', v),
                 size=lambda i, v: setattr(i.rect, 'size', v))
        
        item.add_widget(Label(
            text=f"{treatment['patient_name']} - {treatment['procedure']}",
            font_size='16sp',
            bold=True,
            halign='left',
            size_hint_y=0.4
        ))
        item.add_widget(Label(
            text=f"Date: {treatment['date']} | Cost: ${treatment['cost']}",
            font_size='14sp',
            halign='left',
            size_hint_y=0.3
        ))
        item.add_widget(Label(
            text=f"Notes: {treatment.get('notes', 'N/A')}",
            font_size='12sp',
            halign='left',
            size_hint_y=0.3
        ))
        
        self.treatment_list.add_widget(item)
        
    def show_add_treatment_dialog(self):
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        content.add_widget(Label(text='Patient ID:', size_hint_y=None, height=30))
        patient_input = TextInput(multiline=False, size_hint_y=None, height=40, hint_text='e.g., P0001')
        content.add_widget(patient_input)
        
        content.add_widget(Label(text='Procedure:', size_hint_y=None, height=30))
        procedure_input = TextInput(multiline=False, size_hint_y=None, height=40)
        content.add_widget(procedure_input)
        
        content.add_widget(Label(text='Date:', size_hint_y=None, height=30))
        date_input = TextInput(multiline=False, size_hint_y=None, height=40, hint_text='YYYY-MM-DD')
        content.add_widget(date_input)
        
        content.add_widget(Label(text='Cost:', size_hint_y=None, height=30))
        cost_input = TextInput(multiline=False, size_hint_y=None, height=40)
        content.add_widget(cost_input)
        
        content.add_widget(Label(text='Notes:', size_hint_y=None, height=30))
        notes_input = TextInput(multiline=True, size_hint_y=None, height=60)
        content.add_widget(notes_input)
        
        buttons = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        popup = Popup(title='Add Treatment Record', content=content, size_hint=(0.9, 0.8))
        
        save_btn = Button(text='Save', background_color=(0.3, 0.7, 0.3, 1))
        save_btn.bind(on_press=lambda x: self.save_treatment(
            patient_input.text, procedure_input.text, date_input.text, 
            cost_input.text, notes_input.text, popup))
        buttons.add_widget(save_btn)
        
        cancel_btn = Button(text='Cancel', background_color=(0.7, 0.3, 0.3, 1))
        cancel_btn.bind(on_press=popup.dismiss)
        buttons.add_widget(cancel_btn)
        
        content.add_widget(buttons)
        popup.open()
        
    def save_treatment(self, patient_id, procedure, date, cost, notes, popup):
        if not patient_id or not procedure or not date or not cost:
            return
            
        patients = self.data_mgr.get_patients()
        patient = patients.get(patient_id)
        
        if not patient:
            return
            
        treatments = self.data_mgr.get_treatments()
        treatment_id = f"T{len(treatments) + 1:04d}"
        
        treatments[treatment_id] = {
            'patient_id': patient_id,
            'patient_name': patient['name'],
            'procedure': procedure,
            'date': date,
            'cost': cost,
            'notes': notes,
            'created_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        
        self.data_mgr.save_treatments(treatments)
        popup.dismiss()
        self.build_ui()
        
    def go_back(self):
        self.manager.current = 'home'


class DentalApp(App):
    """Main application class"""
    
    def build(self):
        self.title = 'Dental Practice Manager'
        
        sm = ScreenManager()
        sm.add_widget(HomeScreen())
        sm.add_widget(PatientsScreen())
        sm.add_widget(AppointmentsScreen())
        sm.add_widget(DentalChartScreen())
        sm.add_widget(TreatmentsScreen())
        
        return sm


if __name__ == '__main__':
    DentalApp().run()
