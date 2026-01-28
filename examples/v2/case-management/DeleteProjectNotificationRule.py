"""
Delete a notification rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.delete_project_notification_rule(
        project_id="project_id",
        notification_rule_id="notification_rule_id",
    )
