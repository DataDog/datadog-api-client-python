"""
Get a role returns "OK" response
"""

from os import environ
from datadog_api_client.v2 import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

# there is a valid "role" in the system
ROLE_DATA_ID = environ["ROLE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.get_role(role_id=ROLE_DATA_ID)

    print(response)
