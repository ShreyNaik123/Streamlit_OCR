import streamlit as st

def_dialog():
  if "show_dialog" not in st.session_state:
      st.session_state.show_dialog = False

  # Function to open the modal
  def open_dialog():
      st.session_state.show_dialog = True

  # Function to close the modal
  def close_dialog():
      st.session_state.show_dialog = False

  # Show button to add API key
  if st.button("Add API KEY", type="primary"):
      open_dialog()

  # Simulated modal pop-up
  if st.session_state.show_dialog:
      with st.container(border=True):
          st.write("Have your own API key?")
          
          apiKey = st.text_input("Gemini API Key")
          
          if st.button("Submit"):
              st.write(f"Sending API call to Gemini with {apiKey}")
              # model.init_chat(apiKey)  # Uncomment if `model` is defined
              close_dialog()  # Close the modal after submission
          
          if st.button("Cancel"):
              close_dialog()  # Close modal without submitting