import requests

mackerel_api_endpoint_base = 'https://api.mackerelio.com'


class makapi:
    # Mackerel API
    def __init__(self, mackerel_apikey):
        self.api_endpoint = mackerel_api_endpoint_base + '/api/v0'
        self.headers = {
            'Content-type': 'application/json',
            'X-Api-Key': mackerel_apikey,
        }

        r = self.get('org')
        if "error" in r:
            # APIキーが誤っていた場合はメッセージを返す
            self.organization_name = None
            self.message = r['error']
        else:
            self.organization_name = r['name']

    def build_url(self, api):
        return f'{self.api_endpoint}/{api}'

    def get(self, api):
        ret = requests.get(
            self.build_url(api),
            headers=self.headers,
        ).json()
        return ret

    def post(self, api, payloads):
        ret = requests.post(
            self.build_url(api),
            headers=self.headers,
            data=payloads
        ).json()
        return ret

    def put(self, api):
        ret = requests.put(
            self.build_url(api),
            headers=self.headers,
        ).json()
        return ret

    def delete(self, api):
        ret = requests.delete(
            self.build_url(api),
            headers=self.headers,
        ).json()
        return ret


"""
確認用
"""
if __name__ == '__main__':
    import os

    # Mackerel APIテスト（MACKEREL_APIKEYが設定されていたときのみ）
    mackerel_apikey = os.environ.get('MACKEREL_APIKEY')

    if mackerel_apikey:
        m = makapi(mackerel_apikey)
        if m.organization_name:
            print(f'Organization Name: {m.organization_name}')
        else:
            # 名前が返ってこなかったら失敗
            print(f'Error: {m.message}')

        # print(m.get("hosts"))
    else:
        print('MACKEREL_APIKEY is not set.')
