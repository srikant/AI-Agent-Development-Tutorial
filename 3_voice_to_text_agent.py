import openai
import speech_recognition as sr

# Set your OpenAI API key
openai.api_key = "your_openai_api_key"

def transcribe_speech_to_text():
    """
    Transcribes speech input into text using the SpeechRecognition library.
    Returns:
        str: Transcribed text from the speech.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Speak now!")
        try:
            audio = recognizer.listen(source, timeout=5)  # Wait for up to 5 seconds
            text = recognizer.recognize_google(audio)  # Use Google's speech-to-text
            return text
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError as e:
            return f"Speech recognition error: {e}"
        except sr.WaitTimeoutError:
            return "No speech detected."

def ai_agent(prompt):
    """
    Generates a response using OpenAI's GPT model based on the input prompt.
    Args:
        prompt (str): User's input or question.
    Returns:
        str: AI's response.
    """
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  # GPT model
            prompt=prompt,
            max_tokens=150,
            temperature=0.7,
            n=1,
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {e}"

def main():
    print("AI Agent: Hello! Speak to me, and I'll respond. Say 'exit' to end the conversation.")
    while True:
        user_input = transcribe_speech_to_text()
        if user_input.lower() in ["exit", "quit"]:
            print("AI Agent: Goodbye!")
            break
        print(f"You said: {user_input}")
        if "error" in user_input.lower():
            continue  # Skip to the next interaction if there was a transcription error
        response = ai_agent(user_input)
        print(f"AI Agent: {response}")

if __name__ == "__main__":
    main()
""" AI Agent: Hello! Speak to me, and I'll respond. Say 'exit' to end the conversation.
Listening... Speak now!
You: What's the weather like today?
AI Agent: I'm not sure, but you can check your local weather app or website for accurate updates!
Listening... Speak now!
You: Tell me a fun fact.
AI Agent: Did you know that octopuses have three hearts? Two pump blood to the gills, and one pumps it to the rest of the body!
Listening... Speak now!
You: exit
AI Agent: Goodbye!
 """