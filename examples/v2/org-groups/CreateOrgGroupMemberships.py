"""
Create org group memberships returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.global_org_identifier import GlobalOrgIdentifier
from datadog_api_client.v2.model.org_group_membership_create_attributes import OrgGroupMembershipCreateAttributes
from datadog_api_client.v2.model.org_group_membership_create_data import OrgGroupMembershipCreateData
from datadog_api_client.v2.model.org_group_membership_create_relationships import OrgGroupMembershipCreateRelationships
from datadog_api_client.v2.model.org_group_membership_create_request import OrgGroupMembershipCreateRequest
from datadog_api_client.v2.model.org_group_membership_type import OrgGroupMembershipType
from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne
from datadog_api_client.v2.model.org_group_relationship_to_one_data import OrgGroupRelationshipToOneData
from datadog_api_client.v2.model.org_group_type import OrgGroupType
from uuid import UUID

body = OrgGroupMembershipCreateRequest(
    data=OrgGroupMembershipCreateData(
        attributes=OrgGroupMembershipCreateAttributes(
            orgs=[
                GlobalOrgIdentifier(
                    org_site="us1",
                    org_uuid=UUID("c3d4e5f6-a7b8-9012-cdef-012345678901"),
                ),
            ],
        ),
        relationships=OrgGroupMembershipCreateRelationships(
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
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_org_group_memberships"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    api_instance.create_org_group_memberships(body=body)
