"""
Get an automation rule returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    response = api_instance.get_case_automation_rule(
        project_id="project_id",
        rule_id="rule_id",
    )

    print(response)
