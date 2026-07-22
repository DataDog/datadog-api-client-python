"""
Update an automation rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.automation_rule_action import AutomationRuleAction
from datadog_api_client.v2.model.automation_rule_action_data import AutomationRuleActionData
from datadog_api_client.v2.model.automation_rule_action_type import AutomationRuleActionType
from datadog_api_client.v2.model.automation_rule_create_attributes import AutomationRuleCreateAttributes
from datadog_api_client.v2.model.automation_rule_trigger import AutomationRuleTrigger
from datadog_api_client.v2.model.automation_rule_trigger_data import AutomationRuleTriggerData
from datadog_api_client.v2.model.automation_rule_trigger_type import AutomationRuleTriggerType
from datadog_api_client.v2.model.automation_rule_update import AutomationRuleUpdate
from datadog_api_client.v2.model.automation_rule_update_request import AutomationRuleUpdateRequest
from datadog_api_client.v2.model.case_automation_rule_resource_type import CaseAutomationRuleResourceType
from datadog_api_client.v2.model.case_automation_rule_state import CaseAutomationRuleState

body = AutomationRuleUpdateRequest(
    data=AutomationRuleUpdate(
        attributes=AutomationRuleCreateAttributes(
            action=AutomationRuleAction(
                data=AutomationRuleActionData(
                    handle="workflow-handle-123",
                ),
                type=AutomationRuleActionType.EXECUTE_WORKFLOW,
            ),
            name="Auto-assign workflow",
            state=CaseAutomationRuleState.ENABLED,
            trigger=AutomationRuleTrigger(
                data=AutomationRuleTriggerData(),
                type=AutomationRuleTriggerType.CASE_CREATED,
            ),
        ),
        type=CaseAutomationRuleResourceType.RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.update_case_automation_rule(project_id="project_id", rule_id="rule_id", body=body)

    print(response)
