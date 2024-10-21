# AI-Background-Changer

## Overview
This project uses the Cloudinary AI API to change the background of an uploaded image based on a user-provided prompt. It's built using **Streamlit** for the front-end, and integrates **Cloudinary** for image processing. The user can upload an image, input a prompt, and see a transformed image with an AI-generated background.

## Features
- Upload images in JPG, JPEG, or PNG format.
- Enter a text prompt for background transformation (e.g., "futuristic city at night").
- View the transformed image in real-time.
- Download the transformed image directly from the app.

## How It Works
1. The user uploads an image.
2. The user enters a prompt (such as "forest at sunset").
3. The app sends the image and prompt to Cloudinary's AI API.
4. Cloudinary processes the image and replaces the background based on the prompt.
5. The user can view and download the transformed image.

## Technologies Used
- **Python**: Backend logic.
- **Streamlit**: Frontend for user interaction.
- **Cloudinary**: API for image transformation.
- **Pillow (PIL)**: For image manipulation.
- **Requests**: For handling API calls.

## How to Run Locally

### Prerequisites
- Python 3.x installed on your system.
- A Cloudinary account (for API credentials).

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/arya-io/AI-Background-Changer.git
   cd AI-Background-Changer

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
3. **Set up your Cloudinary credentials:**
    Copy the config_example.py file
   ```bash
   cp config_example.py config.py
   
