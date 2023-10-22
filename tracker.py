from yandex_tracker_client import TrackerClient
from flask import Flask
from requests import get
from config import *


app = Flask(__name__)
client = TrackerClient(token=my_token, cloud_org_id=my_org_id)
response = get("https://api.tracker.yandex.net/v2/myself", headers={"Authorization": my_token,
                                                                    "X-Cloud-Org-ID": my_org_id})
print(response)



# client.issues.create(
# queue='MYQUEUE', summary='API Test Issue', type={'name': 'Bug'}, description='test description'
# )

# issue = client.issues['BRUNERTEST-1']
#
# if __name__ == '__main__':
#     app.run()
