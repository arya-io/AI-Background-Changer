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

## Image Showcase

### Original Image
![Original Image](OriginalImage1.jpg)

### Transformed Images
1. ![Transformed Image 1](transformed_image.jpg)
2. ![Transformed Image 2](transformed_image(1).jpg)
3. ![Transformed Image 3](transformed_image(2).jpg)
4. ![Transformed Image 4](transformed_image(3).jpg)


## Technologies Used
- **Python**: Backend logic.
- **Streamlit**: Frontend for user interaction.
- **Cloudinary**: API for image transformation.
- **Pillow (PIL)**: For image manipulation.
- **Requests**: For handling API calls.

## How to Run Locally

### Prerequisites
- Python installed on your system.
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
    Copy `config_template.py` to `config.py` and fill in your Cloudinary credentials.
   ```bash
   cp config_example.py config.py

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run app.py
2. Open your web browser and go to `http://localhost:8501` to access the app.
3. Upload an image and enter a prompt describing the background you'd like. Click "Submit" to transform the image. You can then download the transformed image.

## Contributing
Contributions are welcome! If you have suggestions or improvements, please feel free to:
- Open an issue to discuss any changes you'd like to see.
- Submit a pull request with your proposed changes.

Please make sure to follow the project's coding style and include tests for any new features.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
