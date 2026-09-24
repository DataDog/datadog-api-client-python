"""
Get On-Call team routing rules returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_on_call_team_routing_rules(
        team_id="27590dae-47be-4a7d-9abf-8f4e45124020",
    )

    print(response)
