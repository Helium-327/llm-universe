from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

import qianfan

def gen_wenxin_messages(prompt):
    """
    构建文心模型的请求参数 messages

    请求参数:
        prompt: 对应的用户提示词
    """
    messages = [{"role" : "user","content": prompt}]
    return messages

def get_completion(prompt, model="ERNIE-Bot", temperature = 0.01):
    """
    获取文心模型调用结果

    请求参数:
        prompt: 对应的用户提示词
        model: 调用的模型名称，可选值：ERNIN-Bot-4
        temperature: 温度系数
    """
    chat_comp = qianfan.ChatCompletion()
    messages = gen_wenxin_messages(prompt)

    response = chat_comp.do(messages=messages,
                            model=model,
                            temperature= temperature,
                            system="你是一名个人助理-小鲸鱼")
    return response['result']

def get_the_model():
    
    model_list = [
        "ERNIE-Bot",  
        "Yi-34B-Chat"]
    
    [print(f"{i}: {v}") for i, v in enumerate(model_list)]
    num_model = input("请选择模型: ")
    model = model_list[int(num_model)]
    return model

if __name__ == '__main__':
    prompt = input("请输入提示词: ")
    model = get_the_model()
    # get_completion(prompt, model=model)
    # result = get_completion("你好，介绍一下你自己", model = "Yi-34B-Chat")
    result = get_completion(prompt=prompt, model=model)
    
    print(result)
