import streamlit as st
from PIL import Image # PIL (Python Imaging Library): Used for handling images in Python
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
# from config import cloud_name, api_key, api_secret
from cloudinary import CloudinaryImage
import uuid # uuid: Generates unique identifiers (used to name uploaded images uniquely)
from io import BytesIO # BytesIO: Allows handling file data in memory (used to process uploaded images)
import requests

st.set_page_config(
    page_title = 'AI Background Changer',
    page_icon = '⚡',
)

# Configure Cloudinary with your cloud name, API key, and API secret
cloudinary.config( 
    cloud_name = st.secrets["CLOUD_NAME"], 
    api_key = st.secrets["API_KEY"], 
    api_secret = st.secrets["API_SECRET"], 
    secure=True  # Ensures that the connection to Cloudinary is secure (https)
)

# Title of the Streamlit app
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🔮 Background Changer with AI 🧠</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #FF5722;'>🚀 AI-Powered Image Transformation ⚡</h3>", unsafe_allow_html=True)

# File uploader widget to allow the user to upload an image (jpg, jpeg, png)
st.markdown("<p style='text-align: center; color: #42a5f5;'>Upload an image to start the magic 🎨</p>", unsafe_allow_html=True)
uploaded_image = st.file_uploader("", type=["jpg", "jpeg", "png"])
# uploaded_image = st.camera_input("")
# uploaded_image = st.file_uploader("", type=["jpg", "jpeg", "png"]) or st.camera_input("")

# If an image is uploaded, show it along with the prompt input
if uploaded_image is not None:
    # Open the uploaded image using PIL and display it in the app
    st.success('Photo uploaded successfully!')
    image = Image.open(uploaded_image)
    st.image(image, use_column_width=True)
    st.markdown("<p style='text-align: center; color: white;'>Original Image</p>", unsafe_allow_html=True)
    
    # Prompt the user to enter a text description for changing the image background
    st.markdown("<p style='text-align: center;'>💡 <i>Describe the background you'd like!</i> 🎨</p>", unsafe_allow_html=True)
    prompt = st.text_input("Enter background description", placeholder="E.g., 'futuristic city at night'", label_visibility="collapsed")

    # Add a button that acts like a submit/enter button
    submit = st.button("Submit")

    # If the user has entered a prompt, start the background transformation process
    if prompt:
        with st.spinner('⏳ Transforming... Hang tight!'):
            # Generate a unique public ID for the uploaded image using uuid for uniqueness
            unique_public_id = f"image_{uuid.uuid4()}"

            # Convert the uploaded image to a BytesIO object (like a file) for uploading to Cloudinary
            img_bytes = BytesIO(uploaded_image.getvalue())

            # Upload the image to Cloudinary with the unique public ID
            cloudinary.uploader.upload(img_bytes, public_id=unique_public_id)

            # Apply the background change transformation based on the user prompt using Cloudinary's AI
            transformation = CloudinaryImage(unique_public_id).image(effect=f"gen_background_replace:prompt_{prompt}")

            # Extract the URL of the transformed image from the HTML response
            start_pos = transformation.find('src="') + len('src="')
            end_pos = transformation.find('"', start_pos)
            transformed_image_url = transformation[start_pos:end_pos]

            # Display the transformed image in the Streamlit app
            st.markdown("<h2 style='text-align: center; color: #E91E63;'>✨ Transformed Image ✨</h2>", unsafe_allow_html=True)
            st.image(transformed_image_url, caption="Transformed with AI 🧠", use_column_width=True)

            # Download the transformed image from Cloudinary using its URL
            try:
                response = requests.get(transformed_image_url)
                response.raise_for_status()  # Raises an error for bad responses (4xx or 5xx)

                image_data = response.content

                # Customizing the download button
                st.markdown("""
                    <style>
                    .stDownloadButton button {
                        background-color: #FF5722;
                        color: white;
                        font-weight: bold;
                        border-radius: 8px;
                        border: 2px solid white;
                        padding: 10px 20px;
                        transition: background-color 0.3s ease;
                    }
                    .stDownloadButton button:hover {
                        background-color: #42a5f5;
                        border-color: #4CAF50;
                    }
                    </style>
                """, unsafe_allow_html=True)
        
                # Add a download button to allow the user to download the transformed image
                st.download_button(
                label="Download Image",   # Text displayed on the button
                data=image_data,          # The image data to be downloaded
                file_name="transformed_image.jpg",  # The default name for the downloaded file
                mime="image/jpeg"         # The file type (JPEG in this case)
                )

            except requests.exceptions.HTTPError as err:
                # Check if it's a 404 error
                if err.response.status_code == 404:
                    st.error("⚠️ The image could not be found. This may be due to the credit limit being reached.")
                else:
                    st.error("⚠️ An error occurred while trying to download the image. Click Submit again.")

# Footer with social media links and credit
st.markdown("""
    <footer>
    <div style="text-align: center; padding: 15px; font-size: 0.9em; color: #888;">
        <p>Made with 💻 by <a href='https://linkedin.com/in/aryaai' style="color: #FF5722; text-decoration: none;">Arya</a></p>
        <div style="padding-top: 5px;">
            <a href='https://linkedin.com/in/aryaai' style="margin-right: 10px;" target='_blank'>
                <img src='https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png' width='24px' alt='LinkedIn' />
            </a>
            <a href='https://github.com/arya-io' target='_blank'>
                <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' width='24px' alt='GitHub' />
            </a>
        </div>
    </div>
    </footer>
""", unsafe_allow_html=True)


