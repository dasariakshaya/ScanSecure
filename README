# ScanSecure – DL and Vehicle Verification Portal

ScanSecure is a web-based portal built to scan Driver’s Licenses (DL) and vehicle number plates using OCR (Optical Character Recognition) and verify them against a backend database. The system is capable of flagging blacklisted drivers or vehicles and provides an admin interface for managing verification logs and blacklists.

## Features

- DL and Number Plate Scanning using OCR
- Data verification against MongoDB records
- Blacklist management for flagged entries
- Admin panel for reviewing scan logs and maintaining records
- RESTful API integration between frontend and backend

## Tech Stack

**Frontend**: HTML, CSS, JavaScript  
**Backend**: Node.js, Express.js, Python (for OCR handling)  
**OCR Engine**: Tesseract OCR  
**Database**: MongoDB

## Project Structure
ScanSecure/
├── client/ # Frontend files (HTML, CSS, JS)
├── server/ # Node.js + Express backend
│ ├── routes/ # API endpoints
│ └── controllers/ # Logic handlers
├── ocr-service/ # Python scripts for OCR (Tesseract)
├── models/ # MongoDB schemas
├── config/ # DB and app config
├── public/ # Static assets
├── app.js # Express entry point
├── README.md
└── package.json


## Installation and Setup

### Prerequisites

- Node.js and npm
- Python 3
- Tesseract OCR installed and configured in system path
- MongoDB running locally or via cloud (MongoDB Atlas)

### Backend Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/ScanSecure.git
cd ScanSecure

2. Install Node dependencies:

```bash
cd server
npm install

3.Set up environment variables (.env file):

```bash
PORT=5000
MONGO_URI=your_mongo_connection_string

4.Start the server:

```bash
node server_r.js

## OCR Service Setup

1. Navigate to the `ScanSecure` directory and install the Python dependencies:

```bash
pip install -r requirements.txt

2. Run the OCR script (this should be integrated or triggered via the backend):

```bash
python ocr_main.py

## How It Works

- The user uploads a DL or vehicle number plate image through the frontend.
- The image is sent to the Python OCR service where Tesseract extracts the relevant information.
- The extracted data is sent to the backend for processing.
- The backend cross-verifies the extracted data with entries in the MongoDB database.
- If the data matches a blacklisted entry, an alert is generated.
- If verification is successful, the entry is logged and marked as valid.
- All scan activities are recorded and can be reviewed via the admin dashboard.

---

## Future Improvements

- Add advanced image pre-processing techniques to enhance OCR accuracy.
- Implement an SMS or email alert system for blacklisted matches.
- Enable CSV export functionality for verification logs.
- Integrate role-based authentication and access control for the admin panel.

