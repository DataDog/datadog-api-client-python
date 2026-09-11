"""
Reorder inbox rules returns "Successfully reordered the inbox rules" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.inbox_rule_reorder_item import InboxRuleReorderItem
from datadog_api_client.v2.model.inbox_rule_reorder_request import InboxRuleReorderRequest
from datadog_api_client.v2.model.inbox_rule_type import InboxRuleType

# there is a valid "valid_inbox_rule" in the system
VALID_INBOX_RULE_DATA_ID = environ["VALID_INBOX_RULE_DATA_ID"]

body = InboxRuleReorderRequest(
    data=[
        InboxRuleReorderItem(
            id=VALID_INBOX_RULE_DATA_ID,
            type=InboxRuleType.INBOX_RULES,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["reorder_security_findings_automation_inbox_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.reorder_security_findings_automation_inbox_rules(body=body)

    print(response)
