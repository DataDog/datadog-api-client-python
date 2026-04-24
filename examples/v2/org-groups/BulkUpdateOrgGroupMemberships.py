"""
Bulk update org group memberships returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.global_org_identifier import GlobalOrgIdentifier
from datadog_api_client.v2.model.org_group_membership_bulk_update_attributes import (
    OrgGroupMembershipBulkUpdateAttributes,
)
from datadog_api_client.v2.model.org_group_membership_bulk_update_data import OrgGroupMembershipBulkUpdateData
from datadog_api_client.v2.model.org_group_membership_bulk_update_relationships import (
    OrgGroupMembershipBulkUpdateRelationships,
)
from datadog_api_client.v2.model.org_group_membership_bulk_update_request import OrgGroupMembershipBulkUpdateRequest
from datadog_api_client.v2.model.org_group_membership_bulk_update_type import OrgGroupMembershipBulkUpdateType
from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne
from datadog_api_client.v2.model.org_group_relationship_to_one_data import OrgGroupRelationshipToOneData
from datadog_api_client.v2.model.org_group_type import OrgGroupType
from uuid import UUID

body = OrgGroupMembershipBulkUpdateRequest(
    data=OrgGroupMembershipBulkUpdateData(
        attributes=OrgGroupMembershipBulkUpdateAttributes(
            orgs=[
                GlobalOrgIdentifier(
                    org_site="us1",
                    org_uuid=UUID("c3d4e5f6-a7b8-9012-cdef-012345678901"),
                ),
            ],
        ),
        relationships=OrgGroupMembershipBulkUpdateRelationships(
            source_org_group=OrgGroupRelationshipToOne(
                data=OrgGroupRelationshipToOneData(
                    id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"),
                    type=OrgGroupType.ORG_GROUPS,
                ),
            ),
            target_org_group=OrgGroupRelationshipToOne(
                data=OrgGroupRelationshipToOneData(
                    id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"),
                    type=OrgGroupType.ORG_GROUPS,
                ),
            ),
        ),
        type=OrgGroupMembershipBulkUpdateType.ORG_GROUP_MEMBERSHIP_BULK_UPDATES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["bulk_update_org_group_memberships"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.bulk_update_org_group_memberships(body=body)

    print(response)
