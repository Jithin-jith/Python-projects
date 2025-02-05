import pyttsx3

def text_to_speech():
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1.0)  # Volume level
    
    # Ask the user for input text
    text = input("Enter the text you want to convert to speech: ")
    
    # Convert text to speech
    engine.say(text)
    
    # Wait for the speech to finish
    engine.runAndWait()

if __name__ == "__main__":
    text_to_speech()