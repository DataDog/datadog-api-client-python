"""
Validate API key returns "OK" response
"""

from datadog_api_client.v1 import ApiClient, Configuration
from datadog_api_client.v1.api.authentication_api import AuthenticationApi

with ApiClient(Configuration()) as api_client:
    api_instance = AuthenticationApi(api_client)
    response = api_instance.validate()

    print(response)
