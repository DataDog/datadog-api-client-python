"""
Update an org group policy override returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.org_group_policy_override_type import OrgGroupPolicyOverrideType
from datadog_api_client.v2.model.org_group_policy_override_update_attributes import (
    OrgGroupPolicyOverrideUpdateAttributes,
)
from datadog_api_client.v2.model.org_group_policy_override_update_data import OrgGroupPolicyOverrideUpdateData
from datadog_api_client.v2.model.org_group_policy_override_update_request import OrgGroupPolicyOverrideUpdateRequest
from uuid import UUID

body = OrgGroupPolicyOverrideUpdateRequest(
    data=OrgGroupPolicyOverrideUpdateData(
        attributes=OrgGroupPolicyOverrideUpdateAttributes(
            org_site="datadoghq.com",
            org_uuid=UUID("c3d4e5f6-a7b8-9012-cdef-012345678901"),
        ),
        id=UUID("9f8e7d6c-5b4a-3210-fedc-ba0987654321"),
        type=OrgGroupPolicyOverrideType.ORG_GROUP_POLICY_OVERRIDES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_org_group_policy_override"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.update_org_group_policy_override(
        org_group_policy_override_id=UUID("9f8e7d6c-5b4a-3210-fedc-ba0987654321"), body=body
    )

    print(response)
