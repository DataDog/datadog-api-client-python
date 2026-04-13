"""
Update an org group membership returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType
from datadog_api_client.v2.model.org_group_membership_update_data import OrgGroupMembershipUpdateData
from datadog_api_client.v2.model.org_group_membership_update_relationships import OrgGroupMembershipUpdateRelationships
from datadog_api_client.v2.model.org_group_membership_update_request import OrgGroupMembershipUpdateRequest
from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne
from datadog_api_client.v2.model.org_group_relationship_to_one_data import OrgGroupRelationshipToOneData
from datadog_api_client.v2.model.org_group_type import OrgGroupType
from uuid import UUID

body = OrgGroupMembershipUpdateRequest(
    data=OrgGroupMembershipUpdateData(
        id=UUID("f1e2d3c4-b5a6-7890-1234-567890abcdef"),
        relationships=OrgGroupMembershipUpdateRelationships(
            org_group=OrgGroupRelationshipToOne(
                data=OrgGroupRelationshipToOneData(
                    id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"),
                    type=OrgGroupType.ORG_GROUPS,
                ),
            ),
        ),
        type=OrgGroupMembershipType.ORG_GROUP_MEMBERSHIPS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_org_group_membership"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.update_org_group_membership(
        org_group_membership_id=UUID("f1e2d3c4-b5a6-7890-1234-567890abcdef"), body=body
    )

    print(response)
