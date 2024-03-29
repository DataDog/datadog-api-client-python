"""
Delete a CSM Threats Agent rule returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_workload_security_api import CloudWorkloadSecurityApi

# there is a valid "agent_rule_rc" in the system
AGENT_RULE_DATA_ID = environ["AGENT_RULE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CloudWorkloadSecurityApi(api_client)
    api_instance.delete_csm_threats_agent_rule(
        agent_rule_id=AGENT_RULE_DATA_ID,
    )
