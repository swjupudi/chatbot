import openai
from settings import load_settings
import pprint

def converse(conversation: list[dict[str,str]])-> str:
    settings = load_settings()
    client = openai.OpenAI(api_key=settings['openai_api_key'])
    # messages = [dict1]
    # dict1 = {}
    # dict1['role'] = 'user'
    # dict1['content'] = user_prompt
   # messages = [{'role':'user', 'content': user_prompt}]
    response = client.chat.completions.create(model = settings['model'], messages = conversation)
    pprint.pprint(response)
    robo_response = response.choices[0].message.content
    return robo_response
