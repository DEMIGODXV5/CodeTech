import os
import sys
import nltk
from nltk.tokenize import word_tokenize
import google.generativeai as genai
from dotenv import load_dotenv

# --- CONFIGURATION ---
# Load environment variables from the .env file
load_dotenv()

# Fetch the key from the environment
API_KEY = os.getenv("GEMINI_API_KEY")

def setup_nltk():
    """
    Ensures necessary NLTK data is downloaded.
    We use NLTK to tokenize sentences, fulfilling the NLP library requirement.
    """
    try:
        nltk.data.find('tokenizers/punkt')
    except LookupError:
        print("Downloading necessary NLTK data...")
        nltk.download('punkt', quiet=True)
        nltk.download('punkt_tab', quiet=True)
        print("NLTK data downloaded.")

def initialize_ai():
    """Configures the Gemini AI model."""
    if not API_KEY:
        print("❌ ERROR: API Key not found.")
        print("Please make sure you have created a '.env' file with GEMINI_API_KEY inside.")
        sys.exit(1)
        
    genai.configure(api_key=API_KEY)
    # Using Flash for speed and efficiency
    model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')
    return model

def process_input_with_nltk(text):
    """
    Demonstrates usage of NLTK for preprocessing.
    In a rule-based bot, this is where we would extract entities.
    Here, we use it to clean and tokenize the prompt.
    """
    # Tokenize the text (split into words/punctuation)
    tokens = word_tokenize(text)
    
    # Example NLP logic: Filter out very short tokens (cleaning)
    clean_tokens = [t for t in tokens if len(t) > 1 or t.isalnum()]
    
    # Reconstruct for the AI
    return " ".join(clean_tokens)

def main():
    # 1. Setup NLP libraries
    print("--- Initializing Chatbot Task 3 ---")
    setup_nltk()
    
    # 2. Setup AI
    try:
        model = initialize_ai()
        chat_session = model.start_chat(history=[])
    except Exception as e:
        print(f"Error connecting to AI: {e}")
        return

    print("\n" + "="*50)
    print("🤖 AI CHATBOT (Python + NLTK + Gemini)")
    print("Type 'exit' or 'quit' to stop.")
    print("="*50 + "\n")

    # 3. Chat Loop
    while True:
        try:
            user_input = input("You: ")
            
            if user_input.lower() in ['exit', 'quit']:
                print("Bot: Goodbye! Have a great day.")
                break
            
            if not user_input.strip():
                continue

            # NLP Step: Preprocess with NLTK
            # This satisfies the requirement to use an NLP library
            processed_text = process_input_with_nltk(user_input)

            # AI Step: Generate content
            # We add a specific instruction to keep it conversational
            response = chat_session.send_message(processed_text)
            
            print(f"Bot: {response.text}")
            print("-" * 30)

        except KeyboardInterrupt:
            print("\nBot: Exiting...")
            break
        except Exception as e:
            print(f"Bot: Oops, I encountered an error: {e}")

if __name__ == "__main__":
    main()