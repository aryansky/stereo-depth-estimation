# Stereo Depth Estimation using Flask (API + CLI)

## Overview

This project implements **stereo depth estimation** using classical computer vision techniques. It takes a pair of stereo images (left and right) and computes a **disparity map**, which represents depth information in the scene.

The system is designed to be:

* Fully executable via **terminal**
* Accessible via a **Flask API**

---

## Features

* Stereo depth estimation using **OpenCV (StereoSGBM)**
* Dual execution modes:

  * CLI (Command Line Interface)
  * API (Flask server)
* Depth map visualization using **color mapping**
* Basic post-processing for noise reduction
* Clean and minimal project structure

---

## Project Structure

```bash
stereo-depth-app/
│
├── app.py
├── requirements.txt
├── README.md
│
├── depth/
│   └── stereo.py
│
├── routes/
│   └── routes.py
│
├── static/
│   └── outputs/
│
└── uploads/
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Running the Project

### Run as API

```bash
python app.py --mode api
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### Run in Terminal

```bash
python app.py --mode cli --left left.png --right right.png
```

Output will be saved in:

```
static/outputs/depth.png
```

---

## API Usage

### Endpoint

```bash
POST /depth
```

### Request (form-data)

* left: left image file
* right: right image file

### Example (curl)

```bash
curl -X POST http://127.0.0.1:5000/depth \
  -F "left=@left.png" \
  -F "right=@right.png"
```

### Response

```json
{
    "message": "Depth map generated",
    "output": "static/outputs\\depth.png"
}
```

---

## How It Works

* Converts stereo images to grayscale
* Uses **StereoSGBM** for disparity estimation
* Normalizes disparity map
* Applies **bilateral filtering** for noise reduction
* Uses **color mapping** for visualization

---

## Limitations

* Requires **rectified stereo images**
* Sensitive to camera alignment
* Performs poorly on textureless regions
* Not suitable for arbitrary phone images

---

## Sample Output

The output is a **colored disparity map**:

* Blue → far objects
* Red/Yellow → near objects

---

## Tech Stack

* Python
* Flask
* OpenCV

---

## Notes

This project demonstrates classical stereo vision concepts including:

* Disparity estimation
* Depth perception
* Correspondence problem

For best results, use dataset images (e.g., Middlebury, InStereo2K).
