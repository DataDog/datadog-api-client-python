"""
Get automatic investigation settings for a monitor returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_ai_api import BitsAIApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_monitor_automation"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsAIApi(api_client)
    response = api_instance.get_monitor_automation(
        monitor_id=9223372036854775807,
    )

    print(response)
