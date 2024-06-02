import requests
import json

def get_access_token(api, secret):
    """
    使用 API Key，Secret Key 获取access_token，替换下列示例中的应用API Key、应用Secret Key
    """

    url = "https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id="+api+"&client_secret="+secret

    payload = json.dumps("")
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.json().get("access_token")


def chat(mes, api, secret):

    url = "https://aip.baidubce.com/rpc/2.0/ai_custom/v1/wenxinworkshop/chat/ernie_speed?access_token=" + get_access_token(api, secret)

    payload = json.dumps({
        "messages": [
            {
                "role": "user",
                "content": mes
            }
        ]
    })
    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    return(json.loads(response.text).get("result"))


if __name__ == '__main__':
    print(chat("你好","6f6WQMFlDin13kUx6QUByUnB","vDplyUXy5XFapNMP2PF47KDyTf0IXX14"))