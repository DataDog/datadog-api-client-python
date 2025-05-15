"""
Delete a Workload Protection agent rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.csm_threats_api import CSMThreatsApi

# there is a valid "agent_rule_rc" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

# there is a valid "policy_rc" in the system
POLICY_DATA_ID = environ["POLICY_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CSMThreatsApi(api_client)
    api_instance.delete_csm_threats_agent_rule(
        agent_rule_id=AGENT_RULE_DATA_ID,
        policy_id=POLICY_DATA_ID,
    )
