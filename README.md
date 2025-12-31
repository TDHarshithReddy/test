# Dental Mobile Application

A comprehensive dental practice management mobile application built with Python and Kivy.

## Features

### 1. **Patient Management**
- Add new patients with complete information (name, phone, email, date of birth)
- View patient list with search and filter capabilities
- View detailed patient profiles
- Unique patient ID generation (P0001, P0002, etc.)

### 2. **Appointment Scheduling**
- Schedule new appointments with patients
- View all appointments sorted by date and time
- Track appointment status (pending/confirmed)
- Link appointments to patient records
- Display today's appointment count on dashboard

### 3. **Dental Chart**
- Interactive dental chart with 32 teeth
- Upper teeth (1-16) and lower teeth (17-32)
- Click on any tooth to view details
- Track tooth conditions and treatment history

### 4. **Treatment Records**
- Record dental procedures and treatments
- Track treatment costs and billing
- Add detailed notes for each treatment
- View treatment history for each patient
- Automatic linking to patient profiles

### 5. **Dashboard**
- Real-time statistics (total patients, today's appointments)
- Quick access to all modules
- Clean and intuitive interface

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone or download this repository

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python main.py
```

## Platform Support

This application runs on:
- **Desktop**: Windows, macOS, Linux
- **Mobile**: Android (with buildozer), iOS (with kivy-ios)

### Building for Android

1. Install buildozer:
```bash
pip install buildozer
```

2. Initialize buildozer configuration:
```bash
buildozer init
```

3. Build the APK:
```bash
buildozer -v android debug
```

### Building for iOS

1. Install kivy-ios tools (macOS only):
```bash
pip install kivy-ios
```

2. Build and deploy to iOS device

## Usage Guide

### Adding a Patient
1. From the home screen, tap "Patients"
2. Tap "+ Add Patient" button
3. Fill in patient information:
   - Name (required)
   - Phone (required)
   - Email (optional)
   - Date of Birth (optional, format: YYYY-MM-DD)
4. Tap "Save" to add the patient

### Scheduling an Appointment
1. From the home screen, tap "Appointments"
2. Tap "+ Schedule" button
3. Enter appointment details:
   - Patient ID (e.g., P0001)
   - Date (format: YYYY-MM-DD)
   - Time (format: HH:MM)
   - Reason for visit
4. Tap "Schedule" to confirm

### Using the Dental Chart
1. From the home screen, tap "Dental Chart"
2. The chart displays 32 teeth (1-32)
3. Tap any tooth number to view details
4. View tooth condition and treatment history

### Recording Treatments
1. From the home screen, tap "Treatments"
2. Tap "+ Add Record" button
3. Enter treatment information:
   - Patient ID
   - Procedure name
   - Date performed
   - Cost
   - Additional notes
4. Tap "Save" to record the treatment

## Data Storage

All data is stored locally in JSON format in the `data/` directory:
- `data/patients.json` - Patient records
- `data/appointments.json` - Appointment records
- `data/treatments.json` - Treatment records

This ensures:
- Fast local access
- Data persistence across app sessions
- Easy backup and migration
- Privacy (no cloud storage by default)

## Architecture

```
main.py                     # Main application file
├── DataManager            # Handles data persistence
├── HomeScreen             # Dashboard with statistics
├── PatientsScreen         # Patient management
├── AppointmentsScreen     # Appointment scheduling
├── DentalChartScreen      # Dental chart visualization
└── TreatmentsScreen       # Treatment records
```

## Customization

### Changing Colors
Edit the color tuples in the button definitions:
```python
background_color=(R, G, B, A)  # Values between 0 and 1
```

### Adding New Features
The modular structure makes it easy to add new screens:
1. Create a new Screen class
2. Add navigation button in HomeScreen
3. Register the screen in DentalApp.build()

## Requirements

- Python 3.7+
- Kivy 2.3.0
- Standard library: json, datetime, os

## Troubleshooting

### Application won't start
- Ensure Python 3.7+ is installed
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check that you're running from the project directory

### Data not saving
- Ensure write permissions in the project directory
- Check that the `data/` folder can be created
- Verify JSON files are not corrupted

### UI issues
- Update Kivy to the latest version
- Check your display resolution
- Try running in windowed mode

## Future Enhancements

Potential features for future versions:
- Patient search and filtering
- Appointment reminders and notifications
- X-ray image storage and viewing
- Insurance claim management
- Multi-user support with authentication
- Cloud synchronization
- Reports and analytics
- Email/SMS notifications
- Payment processing integration
- Multi-language support

## License

This project is provided as-is for educational and commercial use.

## Support

For issues, questions, or contributions, please open an issue in the repository.

---

**Built with ❤️ using Python and Kivy**
