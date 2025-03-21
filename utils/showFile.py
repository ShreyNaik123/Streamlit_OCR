import streamlit as st
def show_file(uploaded_file):
  if uploaded_file is not None:
      # Display file details
      st.write("### Uploaded File Details:")
      st.write(f"**Filename:** {uploaded_file.name}")
      st.write(f"**File Type:** {uploaded_file.type}")
      st.write(f"**Size:** {uploaded_file.size} bytes")

      # Handling different file types
      if uploaded_file.type.startswith("image"):
          st.image(uploaded_file, caption="Uploaded Image", use_container_width =True)
      
      elif uploaded_file.type in ["text/plain", "application/json"]:
          st.write("### File Content:")
          content = uploaded_file.read().decode("utf-8")  # Read as text
          st.text(content)
      
      elif uploaded_file.type == "application/pdf":
          st.write("### PDF Preview:")
          st.write("PDFs cannot be directly previewed, but you can process them.")
          st.download_button("Download PDF", uploaded_file, file_name=uploaded_file.name)
      
      else:
          st.write("File uploaded, but preview is not supported for this type.")