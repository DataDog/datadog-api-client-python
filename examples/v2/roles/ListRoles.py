"""
List roles returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.roles_api import RolesApi

# there is a valid "role" in the system
ROLE_DATA_ATTRIBUTES_NAME = environ["ROLE_DATA_ATTRIBUTES_NAME"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RolesApi(api_client)
    response = api_instance.list_roles(
        filter=ROLE_DATA_ATTRIBUTES_NAME,
    )

    print(response)
