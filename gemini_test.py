from gemini.Gemini import Gemini

if __name__ == "__main__":
  model = Gemini()
  model.init_chat()
  response = model.yap("Hi how are you")  
  print(response)