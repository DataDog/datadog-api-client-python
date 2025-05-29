"""
Get team on-call users returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there are valid "routing_rules" in the system
ROUTING_RULES_DATA_ID = environ["ROUTING_RULES_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    response = api_instance.get_team_on_call_users(
        include="responders,escalations.responders",
        team_id=ROUTING_RULES_DATA_ID,
    )

    print(response)
