"""
Get a Workload Protection policy returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    response = api_instance.get_csm_threats_agent_policy(
        policy_id=POLICY_DATA_ID,
    )

    print(response)
