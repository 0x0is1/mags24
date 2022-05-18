from libhindimagz import *


class Fetcher:
    def __init__(self, mag_id=None, limit=None, img_size=None, issue_id=None, cat_id=None):
        # APIs path
        self.mag_api = '/magazines/apis/v1.1'
        self.user_api = '/user/apis/v1.1'
        self.download_api = '/download/apis/v1.1'

        # http GET type paths
        self.issues_path = f'issues?magId={mag_id}&issueId={issue_id}&imageSize={img_size}&limit={limit}&offset=0'
        self.mags_path = f'issues?magId={mag_id}&limit={limit}&offset=0'
        self.category_path = f'magsbycategory?catId={cat_id}&langIds=1,2&imageSize={img_size}&limit={limit}&offset=0'
        self.issue_det = f'/issueDetails?issueId={issue_id}'

        # http POST type paths
        self.send_otp_path = '/sendOTP'
        self.verify_otp_path = '/verifyOTP'
        self.user_pref_path = '/getuserpref'
        self.refresh_token_path = '/refreshtoken'
        self.download_req_path = '/mags/issuesxod'

        # misc
        self.issue_id = issue_id

        # base header;
        # usable in all but required in some
        self.BASE_HEADERS = {
            'content-type': 'application/json',
            'devicetype': 'pc',
            'os': 'web',
        }

    # http GET functions
    def get_mags(self): return requests.get(
        BASE_URL + self.mag_api + self.mags_path)

    def get_issues(self): return requests.get(
        BASE_URL + self.mag_api + self.issues_path)

    def get_cat(self): return requests.get(
        BASE_URL + self.mag_api + self.category_path)

    def get_issue_det(self): return requests.get(
        BASE_URL + self.mag_api + self.issue_det)

    # http POST functions
    def send_otp(self, number):
        json_data = {
            "number": base64.b64encode(number).decode("utf-8")
        }
        response = requests.post(
            BASE_URL + self.user_api + self.send_otp_path, headers=self.BASE_HEADERS, json=json_data)
        return response

    def verify_otp(self, number, otp):
        json_data = {
            'otp': otp,
            'number': base64.b64encode(number).decode("utf-8"),
            'deviceInfo': {
                'consumptionDeviceName': 'Browser',
                'info': {
                    'type': 'android',
                    'platform': {
                        'name': 'Chrome',
                    },
                    'deviceId': '2087864996',
                },
            },
            'langIds': [
                1,
                2,
            ],
        }
        response = requests.post(
            BASE_URL + self.user_api + self.verify_otp_path, headers=self.BASE_HEADERS, json=json_data)
        return response

    def get_user_pref(self, access_token, uuid):
        headers = {
            'accesstoken': access_token
        }

        json_data = {
            "uuid": uuid, "rec": True, "continue_read": True, "your_papers": True
        }

        response = requests.post(
            BASE_URL + self.user_api + self.user_pref_path, headers=headers, json=json_data)
        return response

    def refresh_token(self, old_mtoken, uuid):
        json_data = {
            "uuid": uuid,
            "mToken": mtoken
        }

        response = requests.post(
            BASE_URL + self.user_api + self.refresh_token_path, json=json_data)
        return response

    def get_magazine(self, access_token, uuid):
        headers = {
            'accesstoken': access_token
        }

        json_data = {
            "uuid": uuid,
            "issueId": self.issue_id
        }

        response = requests.post(BASE_URL + self.download_api +
                                 self.download_req_path, headers=headers, json=json_data)
        return response
