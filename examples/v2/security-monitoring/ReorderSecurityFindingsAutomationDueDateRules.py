"""
Reorder due date rules returns "Successfully reordered the due date rules" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.due_date_rule_reorder_item import DueDateRuleReorderItem
from datadog_api_client.v2.model.due_date_rule_reorder_request import DueDateRuleReorderRequest
from datadog_api_client.v2.model.due_date_rule_type import DueDateRuleType

# there is a valid "valid_due_date_rule" in the system
VALID_DUE_DATE_RULE_DATA_ID = environ["VALID_DUE_DATE_RULE_DATA_ID"]

body = DueDateRuleReorderRequest(
    data=[
        DueDateRuleReorderItem(
            id=VALID_DUE_DATE_RULE_DATA_ID,
            type=DueDateRuleType.DUE_DATE_RULES,
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["reorder_security_findings_automation_due_date_rules"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.reorder_security_findings_automation_due_date_rules(body=body)

    print(response)
