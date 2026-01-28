"""
Remove project from favorites returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
configuration.unstable_operations["unfavorite_project"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.unfavorite_project(
        project_id="project_id",
    )
