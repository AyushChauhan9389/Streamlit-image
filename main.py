import streamlit as st
import google.generativeai as genai
import PIL.Image
import textwrap

# Function to convert text to markdown
def to_markdown(text):
    text = text.replace('•', ' *')
    return textwrap.indent(text, '> ', predicate=lambda _: True)

# Configure Google Generative AI
genai.configure(api_key="AIzaSyAHB8fva0oJVkCPPwBUwUp6t3fVyX_Yxo0")

# Create a Streamlit application
def main():
    st.title("Google Generative AI Image Analysis")

    # Upload the image
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg", "gif", "bmp"])

    if uploaded_file is not None:
        image = PIL.Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")

        # Send the image to Google Generative AI
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content(["Explain whats in this image and its history", image], stream=True)
        response.resolve()

        # Print the response
        st.markdown(to_markdown(response.text))

if __name__ == "__main__":
    main()