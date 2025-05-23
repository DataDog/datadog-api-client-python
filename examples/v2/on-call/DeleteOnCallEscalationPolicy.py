"""
Delete On-Call escalation policy returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.on_call_api import OnCallApi

# there is a valid "escalation_policy" in the system
ESCALATION_POLICY_DATA_ID = environ["ESCALATION_POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OnCallApi(api_client)
    api_instance.delete_on_call_escalation_policy(
        policy_id=ESCALATION_POLICY_DATA_ID,
    )
