"""
Delete a powerpack returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.powerpack_api import PowerpackApi

# there is a valid "powerpack" in the system
POWERPACK_DATA_ID = environ["POWERPACK_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = PowerpackApi(api_client)
    api_instance.delete_powerpack(
        powerpack_id=POWERPACK_DATA_ID,
    )
