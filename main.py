import google.generativeai as genai

# Set your API key
genai.configure(api_key="AIzaSyB5akVxQ1S8PInLwVywJszIl_g5j40btME")

def chat_with_gemini(prompt):
    # Correct spelling here
    model = genai.GenerativeModel("models/gemini-1.5-flash")
    
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    while True:
        user_input = input("YOU: ")
        if user_input.lower() in ["quit", "exit", "bye"]:
            break
        reply = chat_with_gemini(user_input)
        print("BOT:", reply)
