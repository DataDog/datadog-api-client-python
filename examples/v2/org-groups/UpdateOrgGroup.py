"""
Update an org group returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.org_group_type import OrgGroupType
from datadog_api_client.v2.model.org_group_update_attributes import OrgGroupUpdateAttributes
from datadog_api_client.v2.model.org_group_update_data import OrgGroupUpdateData
from datadog_api_client.v2.model.org_group_update_request import OrgGroupUpdateRequest
from uuid import UUID

body = OrgGroupUpdateRequest(
    data=OrgGroupUpdateData(
        attributes=OrgGroupUpdateAttributes(
            name="Updated Org Group Name",
        ),
        id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"),
        type=OrgGroupType.ORG_GROUPS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_org_group"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.update_org_group(org_group_id=UUID("a1b2c3d4-e5f6-7890-abcd-ef0123456789"), body=body)

    print(response)
