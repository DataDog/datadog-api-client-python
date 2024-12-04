"""
Patch SCIM group returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scim_api import ScimApi
from datadog_api_client.v2.model.external_user_group_patch_request import ExternalUserGroupPatchRequest
from datadog_api_client.v2.model.external_user_group_patch_request_operations_items import (
    ExternalUserGroupPatchRequestOperationsItems,
)
from datadog_api_client.v2.model.external_user_group_patch_request_operations_items_op import (
    ExternalUserGroupPatchRequestOperationsItemsOp,
)

body = ExternalUserGroupPatchRequest(
    operations=[
        ExternalUserGroupPatchRequestOperationsItems(
            op=ExternalUserGroupPatchRequestOperationsItemsOp.REPLACE,
            path=None,
            value=dict([("displayName", "Real new group"), ("id", "e43536e9-33fe-43f8-90b8-d3e39a7dd6ad")]),
        ),
        ExternalUserGroupPatchRequestOperationsItems(
            op=ExternalUserGroupPatchRequestOperationsItemsOp.REMOVE,
            path='members[value eq "fddf0cf2-9b60-11ef-ad4b-d6754a54a839"]',
            value=None,
        ),
    ],
    schemas=[
        "urn:ietf:params:scim:api:messages:2.0:PatchOp",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ScimApi(api_client)
    response = api_instance.patch_scim_group(group_id="group_id", body=body)

    print(response)
