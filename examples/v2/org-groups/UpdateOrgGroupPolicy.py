"""
Update an org group policy returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.org_group_policy_enforcement_tier import OrgGroupPolicyEnforcementTier
from datadog_api_client.v2.model.org_group_policy_type import OrgGroupPolicyType
from datadog_api_client.v2.model.org_group_policy_update_attributes import OrgGroupPolicyUpdateAttributes
from datadog_api_client.v2.model.org_group_policy_update_data import OrgGroupPolicyUpdateData
from datadog_api_client.v2.model.org_group_policy_update_request import OrgGroupPolicyUpdateRequest
from uuid import UUID

body = OrgGroupPolicyUpdateRequest(
    data=OrgGroupPolicyUpdateData(
        attributes=OrgGroupPolicyUpdateAttributes(
            content=dict([("value", "UTC")]),
            enforcement_tier=OrgGroupPolicyEnforcementTier.DEFAULT,
        ),
        id=UUID("1a2b3c4d-5e6f-7890-abcd-ef0123456789"),
        type=OrgGroupPolicyType.ORG_GROUP_POLICIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_org_group_policy"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.update_org_group_policy(
        org_group_policy_id=UUID("1a2b3c4d-5e6f-7890-abcd-ef0123456789"), body=body
    )

    print(response)
