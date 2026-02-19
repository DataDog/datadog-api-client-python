"""
Create a change request branch returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.change_management_api import ChangeManagementApi
from datadog_api_client.v2.model.change_request_branch_create_attributes import ChangeRequestBranchCreateAttributes
from datadog_api_client.v2.model.change_request_branch_create_data import ChangeRequestBranchCreateData
from datadog_api_client.v2.model.change_request_branch_create_request import ChangeRequestBranchCreateRequest
from datadog_api_client.v2.model.change_request_branch_resource_type import ChangeRequestBranchResourceType

body = ChangeRequestBranchCreateRequest(
    data=ChangeRequestBranchCreateData(
        attributes=ChangeRequestBranchCreateAttributes(
            branch_name="chm/CHM-1234",
            repo_id="DataDog/dd-source",
        ),
        type=ChangeRequestBranchResourceType.CHANGE_REQUEST_BRANCH,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_change_request_branch"] = True
with ApiClient(configuration) as api_client:
    api_instance = ChangeManagementApi(api_client)
    response = api_instance.create_change_request_branch(change_request_id="change_request_id", body=body)

    print(response)
