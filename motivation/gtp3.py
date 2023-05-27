import os
import openai
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get the OpenAI key from the environment variables
openai.api_key = os.getenv('OPENAI_KEY')

def generate_story(habit, goal):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user",
             "content": f"ChatGPT, could you please write a motivational story in the second person about overcoming challenges to stick with a habit that is difficult to maintain? The reader, who is the protagonist, has a goal of {goal}. The moment of challenge is when they feel inclined not to go for a {habit}. Use inspiring words that describe how they achieve their goal and guide the user in visualizing the scenes. The story should close with the satisfaction they feel after managing to go for a {habit}. Please print the plain story without any intro or comments from yourself. The story should have about 300 words."},
        ],
        max_tokens=500
    )

    story = response['choices'][0]['message']['content']
    return story
