"""
Create an org group policy override returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.org_group_policy_override_create_attributes import (
    OrgGroupPolicyOverrideCreateAttributes,
)
from datadog_api_client.v2.model.org_group_policy_override_create_data import OrgGroupPolicyOverrideCreateData
from datadog_api_client.v2.model.org_group_policy_override_create_relationships import (
    OrgGroupPolicyOverrideCreateRelationships,
)
from datadog_api_client.v2.model.org_group_policy_override_create_request import OrgGroupPolicyOverrideCreateRequest
from datadog_api_client.v2.model.org_group_policy_override_type import OrgGroupPolicyOverrideType
from datadog_api_client.v2.model.org_group_policy_relationship_to_one import OrgGroupPolicyRelationshipToOne
from datadog_api_client.v2.model.org_group_policy_relationship_to_one_data import OrgGroupPolicyRelationshipToOneData
from datadog_api_client.v2.model.org_group_policy_type import OrgGroupPolicyType
from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne
from datadog_api_client.v2.model.org_group_relationship_to_one_data import OrgGroupRelationshipToOneData
from datadog_api_client.v2.model.org_group_type import OrgGroupType
from uuid import UUID

body = OrgGroupPolicyOverrideCreateRequest(
    data=OrgGroupPolicyOverrideCreateData(
        attributes=OrgGroupPolicyOverrideCreateAttributes(
            org_site="us1",
            org_uuid=UUID("c3d4e5f6-a7b8-9012-cdef-012345678901"),
        ),
        relationships=OrgGroupPolicyOverrideCreateRelationships(
            org_group=OrgGroupRelationshipToOne(
                data=OrgGroupRelationshipToOneData(
                    id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"),
                    type=OrgGroupType.ORG_GROUPS,
                ),
            ),
            org_group_policy=OrgGroupPolicyRelationshipToOne(
                data=OrgGroupPolicyRelationshipToOneData(
                    id=UUID("1a2b3c4d-5e6f-7890-abcd-ef0123456789"),
                    type=OrgGroupPolicyType.ORG_GROUP_POLICIES,
                ),
            ),
        ),
        type=OrgGroupPolicyOverrideType.ORG_GROUP_POLICY_OVERRIDES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_org_group_policy_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.create_org_group_policy_override(body=body)

    print(response)
