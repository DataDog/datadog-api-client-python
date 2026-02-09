"""
Create investigation notebook for case returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.notebook_create_data import NotebookCreateData
from datadog_api_client.v2.model.notebook_create_request import NotebookCreateRequest
from datadog_api_client.v2.model.notebook_resource_type import NotebookResourceType

body = NotebookCreateRequest(
    data=NotebookCreateData(
        type=NotebookResourceType.NOTEBOOK,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_case_notebook"] = True
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.create_case_notebook(case_id="case_id", body=body)
