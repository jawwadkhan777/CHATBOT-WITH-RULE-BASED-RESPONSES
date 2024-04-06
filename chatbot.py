# Importing necessary library
import re

# Defining rules and responses
rules = {
    r'hello|hi|hey|good morning|good afternoon|good evening': 'Hello! How can I assist you today?',
    r'how are you': 'I am doing well, thank you! How about you?',
    r'(.*)(fine|well|same to you)':'Great! How can I assist you today?',
    r'(.*)(your name|about yourself)': 'I am a Chatbot. What can I do for you?',
    r'(.*)(age|old) are you': 'I am a computer program, so I do not have an age.',
    r'(.*)(weather|temperature) (?:today|tomorrow|this week)?': 'I am sorry, I cannot provide weather information at the moment.',
    r'(.*)(help|assist|support|information)': 'Sure! I can help you with various tasks. Please specify what you need assistance with.',
    r'(.*)(thank you|thanks)': 'You\'re welcome! If you have any more questions, feel free to ask.',
    r'(.*)(developer|founder) (?:bio|of you|of this chatbot)?': 'Sure! I (chatbot) was developed by Muhammad Jawwad Khan in Python language. He is an undergraduate, pursuing BSCS at University of Karachi (UBIT). He is a motivated and dedicated student with a passion for continuous learning. Seeking opportunities to apply his strong work ethic and maximize his potential.',
    r'(.*)(contact|email|connect)': 'You can contact Muhammad Jawwad Khan via email at m.jawwadkhan777@gmail.com. Connect with him on LinkedIn (https://www.linkedin.com/in/jawwadkhan777/) and check out his GitHub portfolio at (https://github.com/jawwadkhan777).'}

# Function to generate responses based on user input
def chatbot_response(user_input):
    for pattern, response in rules.items():
        if re.match(pattern, user_input.lower()):
            return response
    return "Sorry, I'm currently experiencing a data crunch! My abilities are momentarily constrained."

# Main function to run the chatbot
def main():
    print("----------Welcome to the Rule-Based Chatbot----------")
    print("Note-> Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Goodbye! Have a great day!")
            break
        else:
            response = chatbot_response(user_input)
            print("Chatbot:", response)

if __name__ == "__main__":
    main()
