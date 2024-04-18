import os 
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

os.environ['HTTPS_PROXY'] = 'https://127.0.0.1:7891'
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:7891'

from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url=os.environ.get('OPENAI_BASE_URL'),
)


# 生成ChatCompletion对象，包括了回答文本、创建时间、id等属性。
completion = client.chat.completions.create(
    # 模型版本
    model="gpt-3.5-turbo",
    # 对话列表
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ]
)

if __name__ == "__main__":
    print(completion.choices[0].message.content)