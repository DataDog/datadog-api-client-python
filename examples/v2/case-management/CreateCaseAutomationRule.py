"""
Create an automation rule returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.automation_rule_action import AutomationRuleAction
from datadog_api_client.v2.model.automation_rule_action_data import AutomationRuleActionData
from datadog_api_client.v2.model.automation_rule_action_type import AutomationRuleActionType
from datadog_api_client.v2.model.automation_rule_create import AutomationRuleCreate
from datadog_api_client.v2.model.automation_rule_create_attributes import AutomationRuleCreateAttributes
from datadog_api_client.v2.model.automation_rule_create_request import AutomationRuleCreateRequest
from datadog_api_client.v2.model.automation_rule_trigger import AutomationRuleTrigger
from datadog_api_client.v2.model.automation_rule_trigger_data import AutomationRuleTriggerData
from datadog_api_client.v2.model.automation_rule_trigger_type import AutomationRuleTriggerType
from datadog_api_client.v2.model.case_automation_rule_resource_type import CaseAutomationRuleResourceType
from datadog_api_client.v2.model.case_automation_rule_state import CaseAutomationRuleState

body = AutomationRuleCreateRequest(
    data=AutomationRuleCreate(
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
configuration.unstable_operations["create_case_automation_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_case_automation_rule(project_id="project_id", body=body)

    print(response)
