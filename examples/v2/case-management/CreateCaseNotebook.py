"""
Create investigation notebook for case returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi
from datadog_api_client.v2.model.case_investigation_notebook_create_data import CaseInvestigationNotebookCreateData
from datadog_api_client.v2.model.case_investigation_notebook_create_request import (
    CaseInvestigationNotebookCreateRequest,
)
from datadog_api_client.v2.model.case_investigation_notebook_resource_type import CaseInvestigationNotebookResourceType

body = CaseInvestigationNotebookCreateRequest(
    data=CaseInvestigationNotebookCreateData(
        type=CaseInvestigationNotebookResourceType.NOTEBOOK,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.create_case_notebook(case_id="case_id", body=body)
