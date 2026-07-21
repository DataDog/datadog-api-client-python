"""
Delete an automation rule returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.delete_case_automation_rule(
        project_id="project_id",
        rule_id="rule_id",
    )
