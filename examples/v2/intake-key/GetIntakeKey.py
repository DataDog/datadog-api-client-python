"""
Get an intake API key returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.intake_key_api import IntakeKeyApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = IntakeKeyApi(api_client)
    response = api_instance.get_intake_key()

    print(response)
