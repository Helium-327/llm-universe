import os
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

from zhipuai import ZhipuAI

client = ZhipuAI(
    api_key = os.environ["ZHIPUAI_API_KEY"]
)

def gen_glm_params(prompt):
    """
    构造 GLM 模型请求参数 messages

    请求参数:
        prompt: 对应的用户提示词
    """
    messages = [{"role": "user", "content": prompt}]
    return messages

def get_completion(prompt, 
                   model="glm-4",
                   temperature=0.95):
    """
    获取 GLM 模型生成的回复

    请求参数:
        prompt: 对应的用户提示词
        model: GLM 模型名称，可选值有 glm-4 和 glm-3-turbo
        temperature: 生成回复的多样性，取值范围为 [0, 1]，数值越大，回复越多样
    """
    messages = gen_glm_params(prompt)
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature
    )
    if len(response.choices) > 0:
        return response.choices[0].message.content
    return "generate answer error"

def choose_model():
    model_list = 


if __name__ == "__main__":
    prompt = input("请输入用户提示词:")
    answer = get_completion(prompt=prompt)
    print(answer)