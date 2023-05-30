import os
import openai as ai

from dotenv import dotenv_values, find_dotenv

config = dotenv_values(find_dotenv())

ai.api_key = config['OPENAI_API_KEY']

def query_ai(prompt):
    print('Prompt: ',prompt)
    completions = ai.Completion.create(
        model = "text-davinci-003",
        prompt = prompt,
        temperature = 0.9,
        max_tokens = 265,
        top_p = 1,
        frequency_penalty = 0.0,
        presence_penalty = 0.0,
        stop=None
    )
    message = completions.choices[0].text
    print('Message: ', message)
    return message


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    query_ai(config['QUERY_TEXT'])
    print('It works!')