"""
Create a due date rule returns "Successfully created the due date rule" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.security_monitoring_api import SecurityMonitoringApi
from datadog_api_client.v2.model.automation_rule_scope import AutomationRuleScope
from datadog_api_client.v2.model.due_date_from import DueDateFrom
from datadog_api_client.v2.model.due_date_per_severity_item import DueDatePerSeverityItem
from datadog_api_client.v2.model.due_date_rule_action import DueDateRuleAction
from datadog_api_client.v2.model.due_date_rule_attributes_create import DueDateRuleAttributesCreate
from datadog_api_client.v2.model.due_date_rule_create_request import DueDateRuleCreateRequest
from datadog_api_client.v2.model.due_date_rule_data_create import DueDateRuleDataCreate
from datadog_api_client.v2.model.due_date_rule_type import DueDateRuleType
from datadog_api_client.v2.model.due_date_severity import DueDateSeverity
from datadog_api_client.v2.model.security_finding_type import SecurityFindingType

body = DueDateRuleCreateRequest(
    data=DueDateRuleDataCreate(
        attributes=DueDateRuleAttributesCreate(
            action=DueDateRuleAction(
                due_days_per_severity=[
                    DueDatePerSeverityItem(
                        due_in_days=7,
                        severity=DueDateSeverity.CRITICAL,
                    ),
                ],
                due_from=DueDateFrom.FIRST_SEEN,
            ),
            enabled=True,
            name="Example-Security-Monitoring",
            rule=AutomationRuleScope(
                finding_types=[
                    SecurityFindingType.MISCONFIGURATION,
                ],
                query="env:staging",
            ),
        ),
        type=DueDateRuleType.DUE_DATE_RULES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_security_findings_automation_due_date_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = SecurityMonitoringApi(api_client)
    response = api_instance.create_security_findings_automation_due_date_rule(body=body)

    print(response)
