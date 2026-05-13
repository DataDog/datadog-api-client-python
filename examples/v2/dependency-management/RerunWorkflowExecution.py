"""
Rerun a workflow execution returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dependency_management_api import DependencyManagementApi
from uuid import UUID

configuration = Configuration()
configuration.unstable_operations["rerun_workflow_execution"] = True
with ApiClient(configuration) as api_client:
    api_instance = DependencyManagementApi(api_client)
    response = api_instance.rerun_workflow_execution(
        id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"),
    )

    print(response)
