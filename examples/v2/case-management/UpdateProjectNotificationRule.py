"""
Update a notification rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_notification_rule_attributes import CaseNotificationRuleAttributes
from datadog_api_client.v2.model.case_notification_rule_recipient import CaseNotificationRuleRecipient
from datadog_api_client.v2.model.case_notification_rule_recipient_data import CaseNotificationRuleRecipientData
from datadog_api_client.v2.model.case_notification_rule_resource_type import CaseNotificationRuleResourceType
from datadog_api_client.v2.model.case_notification_rule_trigger import CaseNotificationRuleTrigger
from datadog_api_client.v2.model.case_notification_rule_trigger_data import CaseNotificationRuleTriggerData
from datadog_api_client.v2.model.case_notification_rule_update import CaseNotificationRuleUpdate
from datadog_api_client.v2.model.case_notification_rule_update_request import CaseNotificationRuleUpdateRequest

body = CaseNotificationRuleUpdateRequest(
    data=CaseNotificationRuleUpdate(
        attributes=CaseNotificationRuleAttributes(
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
    api_instance.update_project_notification_rule(
        project_id="project_id", notification_rule_id="notification_rule_id", body=body
    )
