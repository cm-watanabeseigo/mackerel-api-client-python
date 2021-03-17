import requests

mackerel_api_endpoint_base = 'https://api.mackerelio.com'


class makapi:
    # Mackerel API
    def __init__(self, mackerel_apikey):
        self.api_endpoint = mackerel_api_endpoint_base + '/api/v0'
        self.organization_name = None
        self.headers = {
            'Content-type': 'application/json',
            'X-Api-Key': mackerel_apikey,
        }

        r = self.get('org')
        if "error" in r:
            # APIキーが誤っていた場合はメッセージを返す
            self.message = r['error']
        else:
            self.organization_name = r['name']

    def build_url(self, api):
        return f'{self.api_endpoint}/{api}'

    def get(self, api):
        if api == "org" and self.organization_name:
            # 既に取得済みなので API を叩かずに返す
            ret = {"name": self.organization_name}
        else:
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
