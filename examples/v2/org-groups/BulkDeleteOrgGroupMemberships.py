"""
Bulk delete org group memberships returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.org_group_membership_bulk_delete_request import OrgGroupMembershipBulkDeleteRequest
from datadog_api_client.v2.model.org_group_membership_bulk_delete_request_data import (
    OrgGroupMembershipBulkDeleteRequestData,
)
from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType
from uuid import UUID

body = OrgGroupMembershipBulkDeleteRequest(
    data=[
        OrgGroupMembershipBulkDeleteRequestData(
            id=UUID("f1e2d3c4-b5a6-7890-1234-567890abcdef"),
            type=OrgGroupMembershipType.ORG_GROUP_MEMBERSHIPS,
        ),
    ],
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["bulk_delete_org_group_memberships"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    api_instance.bulk_delete_org_group_memberships(
        filter_org_group_id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"), body=body
    )
