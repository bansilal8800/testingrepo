import openai
import os

# Set your OpenAI API key
openai.api_key = ''

def chat_with_gpt(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Specify the model
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,  # Adjust the response length as needed
            temperature=0.7,  # Adjust the creativity level
        )
        return response.choices[0].message['content'].strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage
if __name__ == "__main__":
    user_input = input("You: ")
    response = chat_with_gpt(user_input)
    print("ChatGPT:", response)
