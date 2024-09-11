import streamlit as st
from PIL import Image
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold
import keys


safety_settings = {
    HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
    HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
}


GOOGLE_API_KEY = keys.GOOGLE_API_KEY
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def process_image(image, prompt):
    response = model.generate_content([prompt, image], safety_settings=safety_settings)
    return response

st.set_page_config(page_title="Introduction to Streamlit", layout="wide")

st.title("Upload Image")

input_file = st.file_uploader("Upload in png format",type="png")
instruction = st.text_input("Instruction")

if input_file is not None and instruction > "":
    image = Image.open(input_file)
    response = process_image(image, instruction)
    st.write("Response")
    st.write(response.text)