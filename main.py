# QR Based Event Check-in System

A simple Python mini project that manages entry at an event using QR codes.

**Name:** Shankar Kumar Sahu
**Roll No:** 25/SCA/BCOA/020

## Features
- Register guests and generate a unique ID and QR code for each
- Check in by webcam, QR image, or Guest ID
- Warns if the same QR is scanned twice
- Rejects QR codes that are not registered
- Saves check-in date and time in a CSV file
- Shows the guest list and a summary

## Requirements
- Python 3
- opencv-python and numpy

## How to run
pip install opencv-python numpy
python qr_event_checkin.py

## Technologies
Python, OpenCV, CSV, datetime
