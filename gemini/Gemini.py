import google.generativeai as genai
from google.generativeai import types
import os
from dotenv import load_dotenv
from PIL import Image
import re
import pandas as pd



load_dotenv()


class Gemini:
  def __init__(self, model='gemini-1.5-flash', temperature=1, top_p=0.95, top_k=40,max_output_tokens=8192, response_mime_type='text/plain'):
    
    self.api_key = os.environ.get("GEMINI_API_KEY")   
    self.model = model
    self.temperature= temperature
    self.top_p= top_p
    self.top_k= top_k
    self.max_output_tokens= max_output_tokens
    self.response_mime_type= response_mime_type
    self.chat_session = None
    self.history = []
  
  
  
  def configure_genai(self, api_key=None):
      print("API KEy", api_key)
      if api_key:
        genai.configure(api_key=api_key)
      else:
        genai.configure(api_key=self.api_key)
  
  def set_api_key(self, api_key):
    self.api_key = api_key
  
  def __get_config(self):
    print("Initializing config...")
    return {
        "temperature":self.temperature,
        "top_p":self.top_p,
        "top_k":self.top_k,
        "max_output_tokens":self.max_output_tokens,
        "response_mime_type":self.response_mime_type,
    }
  
  def __get_model(self): 
      print("Initializing model...")
      model = genai.GenerativeModel(
        model_name=self.model,
        generation_config=self.__get_config(),
        system_instruction="""
        You are a Streamlit text extraction assistant that analyzes images and generates ready-to-use Streamlit code.

REQUIREMENTS:
0. DO NOT LOAD ANY IMAGE. DO NOT SHOW ANY IMAGE. NO IMAGES AT ALL. NONE OF THE IMAGES EXISTS TO LOAD IN THE CODE THAT YOU RETURN

0. DO NOT LOAD ANY IMAGE. DO NOT USE st.image("image.jpg") or PIL or any libraryu to load any images

DO NOT INCLUDE ANY IMAGE LOADING LINES

1. DO NOT include ANY import statements - assume all Streamlit imports are already handled
2. Return ONLY executable Streamlit code with no explanations or comments outside the code block
3. Structure the extracted text to match the original layout in the image
4. Use appropriate Streamlit components (tables, columns, headers, etc.) to present the content effectively
5. Do not try to load any image. Do not show any image. NO IMAGES.

IF TEXT IS PRESENT IN THE IMAGE:
- Extract and organize all visible text
- Maintain hierarchy, formatting, and structure from the original image
- Use st.title(), st.header(), st.subheader() for headings
- Use st.table() or st.dataframe() for tabular data
- Use st.columns() to preserve multi-column layouts
- If financial data is present, include appropriate charts (st.bar_chart, st.pie_chart) to visualize spending breakdowns

IF NO TEXT IS PRESENT IN THE IMAGE:
- Create a witty multi-sentence description about what's visible in the image using st.write()
- Include a humorous poem with puns about the image content
- Apply custom styling to the poem using st.markdown() with CSS
- Keep in mind the custom styling should go with black background

DO NOT attempt to load or process the image - assume it has already been analyzed.
        
        """,
        # system_instruction="""
        # DO NOT INCLUDE ANY IMPORT STATEMENT
        # You are a model that given an image scans it and returns the text in it as a structured format. Make it in a format that stremlit can display the content properly and nicely.
        # DO NOT INCLUDE ANY IMPORT STATEMENT
        # Do not return anything but the code. Use tables, charts and other things as well from stremlit. Structure the text as it was on the image. 
        
        # If there is no text in the image, return a witty response explaining what is in the image, DO NOT TRY TO LOAD THE IMAGE. IF THERE IS NO TEXT, YOU SHOULD JUST RETURN IN st.write() with a witty response of the image. MAKE THE WITTY RESPONSE LONGER THAN JUST ONE SENTENCE. DO NOT INCLUDE IMPORT STATEMENTS. 
        # AND IF THERE IS NO TEXT THEN INCLUDE A PUN-FULL POEM ABOUT THE IMAGE. AND STYLE THIS PUN-FULL POEM DIFFERENTLY
        
        # DO NOT INCLUDE THE PUN-FULL POEM IF THERE IS TEXT IN THE IMAGE
        
        
        # Only include charts for bills and other stuff explaining how much was spent on what if the image has information about this
        
        # """,
      )

      return model
  
  def init_chat(self, api_key):
    
    self.configure_genai(api_key)
    print("Initializing chat...")
    if api_key:
      print("With provided api key")
    else:
      print("With inbuilt api key")
    model = self.__get_model()
    self.chat_session = model.start_chat(
      history=self.history
    )
  
  def yap(self, message):
    print("Sending message...")
    response = self.chat_session.send_message(message)
    
    return response.text
  
  
  def visual_yap(self, image_path):
    """Processes an image and sends it to Gemini for analysis."""
    try:
      print("Opening image...")
      image = Image.open(image_path)
      
      
      response = self.chat_session.send_message(image)
      generated_code = response.text.strip()
      generated_code = re.sub(r"^```python\n?", "", generated_code) 
      generated_code = re.sub(r"\n?```$", "", generated_code)  


      print(generated_code)
      # print("Initializing Gemini Client...")
      # client = genai.Client()

      # print("Sending image for analysis...")
      # response = client.models.generate_content(
      #   model="gemini-2.0-flash",
      #   contents=["You are a model that given an image scans it and returns the text in it as a structured format", image]
      # )

      return generated_code 
    except Exception as e:
      print(f"Error processing image: {e}")
      return None