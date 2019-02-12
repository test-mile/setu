import requests
import uuid

from config import ex
from automator_actions import *

print(ex)

agent_base_url = "http://localhost:9898"

automator_uuid = str(uuid.uuid4())

# Launch Chrome using Java Agent
response = requests.post(agent_base_url + "/guiauto/automator/{}/launch".format(automator_uuid), json=ex)
print(response.text)

response = requests.post(
            agent_base_url + "/guiauto/automator/{}/action".format(automator_uuid),
            json=TestAutomatorActionBodyCreator.goTo(url="https://www.google.com?q=Setu")
)
print(response.text)

response = requests.get(agent_base_url + "/guiauto/automator/{}/quit".format(automator_uuid))
print(response.text)