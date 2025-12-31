# Quick Start Guide

Get your Dental Mobile Application up and running in 5 minutes!

## Installation

### Step 1: Install Python
Make sure you have Python 3.7 or higher installed:
```bash
python --version
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Run the Application
```bash
python main.py
```

## First Time Setup

When you first launch the app, you'll see the home screen with zero patients and appointments.

### Add Your First Patient

1. Click **"Patients"** from the home screen
2. Click **"+ Add Patient"**
3. Fill in the details:
   - Name: John Doe
   - Phone: 555-1234
   - Email: john@example.com
   - DOB: 1990-01-15
4. Click **"Save"**

Your first patient is now added with ID **P0001**!

### Schedule Your First Appointment

1. Go back to home and click **"Appointments"**
2. Click **"+ Schedule"**
3. Fill in the details:
   - Patient ID: P0001
   - Date: 2024-01-15
   - Time: 10:00
   - Reason: Regular checkup
4. Click **"Schedule"**

### Record a Treatment

1. Go to **"Treatments"**
2. Click **"+ Add Record"**
3. Fill in the details:
   - Patient ID: P0001
   - Procedure: Teeth Cleaning
   - Date: 2024-01-15
   - Cost: 150
   - Notes: Routine cleaning, no issues found
4. Click **"Save"**

### Explore the Dental Chart

1. Click **"Dental Chart"** from the home screen
2. You'll see an interactive chart with 32 teeth
3. Click on any tooth (1-32) to view its details
4. The chart is organized as:
   - Upper teeth: 1-16
   - Lower teeth: 17-32

## Tips

- **Patient IDs** are automatically generated (P0001, P0002, etc.)
- **Date format** is YYYY-MM-DD (e.g., 2024-01-15)
- **Time format** is HH:MM (e.g., 14:30 for 2:30 PM)
- All data is saved automatically in the `data/` folder
- Use the **← Back** button to return to the home screen

## Testing on Mobile

### Android
```bash
# Install buildozer
pip install buildozer

# Build APK
buildozer android debug

# Install on device
adb install bin/*.apk
```

### iOS (macOS only)
```bash
# Install kivy-ios
pip install kivy-ios

# Follow iOS build instructions
```

## Sample Data

Want to test with sample data? Add multiple patients and explore the features:

**Patient 2:**
- Name: Jane Smith
- Phone: 555-5678
- Email: jane@example.com
- DOB: 1985-05-20

**Patient 3:**
- Name: Bob Wilson
- Phone: 555-9012
- Email: bob@example.com
- DOB: 1978-11-30

## Troubleshooting

**App won't start?**
- Make sure Kivy is installed: `pip install kivy`
- Check Python version: `python --version` (must be 3.7+)

**Can't see the data?**
- Data is stored in the `data/` folder as JSON files
- Check file permissions in your project directory

**UI looks weird?**
- Try resizing the window
- Check your display scaling settings
- Update Kivy: `pip install --upgrade kivy`

## Next Steps

- Customize colors and styling in `main.py`
- Add more patients and appointments
- Explore the dental chart feature
- Build for mobile deployment
- Check `README.md` for advanced features

---

**Happy practicing! 🦷**
