"""
Create an org group returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.org_groups_api import OrgGroupsApi
from datadog_api_client.v2.model.org_group_create_attributes import OrgGroupCreateAttributes
from datadog_api_client.v2.model.org_group_create_data import OrgGroupCreateData
from datadog_api_client.v2.model.org_group_create_request import OrgGroupCreateRequest
from datadog_api_client.v2.model.org_group_type import OrgGroupType

body = OrgGroupCreateRequest(
    data=OrgGroupCreateData(
        attributes=OrgGroupCreateAttributes(
            name="My Org Group",
        ),
        type=OrgGroupType.ORG_GROUPS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_org_group"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrgGroupsApi(api_client)
    response = api_instance.create_org_group(body=body)

    print(response)
