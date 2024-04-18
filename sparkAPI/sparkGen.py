import os
import sparkAPI

from dotenv import load_dotenv, find_dotenv


_ = load_dotenv(find_dotenv())

def gen_spark_params(model):
    """
    构建星火模型请求参数
    """

    spark_url_tpl = "wss://spark-api.xf-yun.com/{}/chat"
    model_params_dict = {
        "v1.5":{
            "domain": "general",
            "spark_url": spark_url_tpl.format("v1.1")
        },
        "v2.0":{
            "domain": "generalv2",
            "spark_url": spark_url_tpl.format("v2.1")
        },
        "v3.0":{
            "domain": "generalv3",
            "spark_url": spark_url_tpl.format("v3.1")
        },
        "v3.5":{
            "domain": "generalv3.5",
            "spark_url": spark_url_tpl.format("v3.5")
        }
    }
    return model_params_dict[model]


def get_completion(prompt, model="v2.0", temperature=0.1):
    """
    获取星火模型调用结果

    请求参数：
        prompt: 对话提示词
        model: 模型版本， 默认为 v3.5, 
        temperature: 温度系数，控制输出的随机程度，取值范围是 0~1.0， 且不能设置为0.

    返回结果：
        sparkAPI.SparkResponse: 星火模型调用结果
    """
    response = sparkAPI.main(
        appid = os.environ["SPARK_APPID"],
        api_secret = os.environ["SPARK_API_SECRET"],
        api_key = os.environ["SPARK_API_KEY"],
        gpt_url = gen_spark_params(model)["spark_url"],
        domain = gen_spark_params(model)["domain"],
        query = prompt
    )
    return response


if __name__ == "__main__":
    # prompt = "你好，星火大模型"
    model = input("请输入模型版本：")
    prompt = input("请输入对话提示词：")
    get_completion(prompt, model=model)