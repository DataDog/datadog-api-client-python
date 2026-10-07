"""
Read automatic investigation settings for a new monitor
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.bits_ai_api import BitsAIApi

# there is a valid "monitor" in the system
MONITOR_ID = environ["MONITOR_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_monitor_automation"] = True
with ApiClient(configuration) as api_client:
    api_instance = BitsAIApi(api_client)
    response = api_instance.get_monitor_automation(
        monitor_id=int(MONITOR_ID),
    )

    print(response)
