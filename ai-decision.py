import openai
import ai_function
import os

client = openai.OpenAI(api_key='OpenAIAPIKEY',)

current_directory = os.path.dirname(os.path.abspath(__file__))
file_name = 'ai_function.py'
file_path = os.path.join(current_directory, file_name)

with open(file_path, 'r') as file_function:
  file_function = file_function.read()

while True:

  query = input('How can I help?   ')
  os.system('clear')

  if 'exit' in query:
    break

  response = client.chat.completions.create(
    messages=[
      {"role": "system", "content": "You are assisting in choosing the most suitable Python function for a user request."},
      {"role": "assistant", "content": "You will be provided with available function names for this program."},
      {"role": "assistant", "content": "Please only provide the name of the function, without additional information or responses."},
      {"role": "assistant", "content": "Do not provide any response other than the correct function name."},
      {"role": "assistant", "content": file_function},
      {"role": "user", "content": query}
    ],
    model="gpt-3.5-turbo",
  )

  response = response.choices[0].message.content
  print(f'OpenAI response: {response}')

  if 'hello' in response:
    answer = ai_function.hello()
  elif 'goodbye' in response:
    answer = ai_function.goodbye()
  elif 'understand' in response:
    answer = ai_function.dont_understand()  
  elif 'time' in response:
    answer = ai_function.get_time()
  elif 'weather' in response:
    answer = ai_function.get_weather()
  elif 'joke' in response:
    answer = ai_function.get_joke(query)

  print(f'Message: {answer}')
