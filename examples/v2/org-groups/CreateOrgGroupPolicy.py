"""
Create an org group policy returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.org_group_policy_create_attributes import OrgGroupPolicyCreateAttributes
from datadog_api_client.v2.model.org_group_policy_create_data import OrgGroupPolicyCreateData
from datadog_api_client.v2.model.org_group_policy_create_relationships import OrgGroupPolicyCreateRelationships
from datadog_api_client.v2.model.org_group_policy_create_request import OrgGroupPolicyCreateRequest
from datadog_api_client.v2.model.org_group_policy_type import OrgGroupPolicyType
from datadog_api_client.v2.model.org_group_relationship_to_one import OrgGroupRelationshipToOne
from datadog_api_client.v2.model.org_group_relationship_to_one_data import OrgGroupRelationshipToOneData
from datadog_api_client.v2.model.org_group_type import OrgGroupType
from uuid import UUID

body = OrgGroupPolicyCreateRequest(
    data=OrgGroupPolicyCreateData(
        attributes=OrgGroupPolicyCreateAttributes(
            content=dict([("value", "UTC")]),
            policy_name="monitor_timezone",
        ),
        relationships=OrgGroupPolicyCreateRelationships(
            org_group=OrgGroupRelationshipToOne(
                data=OrgGroupRelationshipToOneData(
                    id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"),
                    type=OrgGroupType.ORG_GROUPS,
                ),
            ),
        ),
        type=OrgGroupPolicyType.ORG_GROUP_POLICIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_org_group_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.create_org_group_policy(body=body)

    print(response)
