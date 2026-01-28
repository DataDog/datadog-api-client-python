"""
Create a notification rule returns "CREATED" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_notification_rule_create import CaseNotificationRuleCreate
from datadog_api_client.v2.model.case_notification_rule_create_attributes import CaseNotificationRuleCreateAttributes
from datadog_api_client.v2.model.case_notification_rule_create_request import CaseNotificationRuleCreateRequest
from datadog_api_client.v2.model.case_notification_rule_recipient import CaseNotificationRuleRecipient
from datadog_api_client.v2.model.case_notification_rule_recipient_data import CaseNotificationRuleRecipientData
from datadog_api_client.v2.model.case_notification_rule_resource_type import CaseNotificationRuleResourceType
from datadog_api_client.v2.model.case_notification_rule_trigger import CaseNotificationRuleTrigger
from datadog_api_client.v2.model.case_notification_rule_trigger_data import CaseNotificationRuleTriggerData

body = CaseNotificationRuleCreateRequest(
    data=CaseNotificationRuleCreate(
        attributes=CaseNotificationRuleCreateAttributes(
            is_enabled=True,
            recipients=[
                CaseNotificationRuleRecipient(
                    data=CaseNotificationRuleRecipientData(),
                    type="EMAIL",
                ),
            ],
            triggers=[
                CaseNotificationRuleTrigger(
                    data=CaseNotificationRuleTriggerData(),
                    type="CASE_CREATED",
                ),
            ],
        ),
        type=CaseNotificationRuleResourceType.NOTIFICATION_RULE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.create_project_notification_rule(project_id="project_id", body=body)

    print(response)
