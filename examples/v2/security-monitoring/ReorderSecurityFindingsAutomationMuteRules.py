"""
Reorder mute rules returns "Successfully reordered the mute rules" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.mute_rule_reorder_item import MuteRuleReorderItem
from datadog_api_client.v2.model.mute_rule_reorder_request import MuteRuleReorderRequest
from datadog_api_client.v2.model.mute_rule_type import MuteRuleType

# there is a valid "valid_mute_rule" in the system
VALID_MUTE_RULE_DATA_ID = environ["VALID_MUTE_RULE_DATA_ID"]

body = MuteRuleReorderRequest(
    data=[
        MuteRuleReorderItem(
            id=VALID_MUTE_RULE_DATA_ID,
            type=MuteRuleType.MUTE_RULES,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["reorder_security_findings_automation_mute_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.reorder_security_findings_automation_mute_rules(body=body)

    print(response)
