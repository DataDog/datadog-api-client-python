"""
Delete an Application key returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.key_management_api import KeyManagementApi

# there is a valid "application_key" in the system
APPLICATION_KEY_DATA_ID = environ["APPLICATION_KEY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = KeyManagementApi(api_client)
    api_instance.delete_application_key(
        app_key_id=APPLICATION_KEY_DATA_ID,
    )
