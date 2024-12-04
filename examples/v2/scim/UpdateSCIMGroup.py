"""
Update SCIM group returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.scim_api import ScimApi
from datadog_api_client.v2.model.external_user_group import ExternalUserGroup
from datadog_api_client.v2.model.external_user_group_members_items import ExternalUserGroupMembersItems
from datadog_api_client.v2.model.external_user_group_meta import ExternalUserGroupMeta

body = ExternalUserGroup(
    members=[
        ExternalUserGroupMembersItems(
            _ref="https://app.datadoghq.com/api/scim/v2/Users/429ebce5-8ed3-4da9-9f1e-662f2dbc2fe6",
            type="User",
        ),
    ],
    meta=ExternalUserGroupMeta(
        resource_type="Group",
    ),
    schemas=[
        "urn:ietf:params:scim:schemas:core:2.0:Group",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ScimApi(api_client)
    response = api_instance.update_scim_group(group_id="group_id", body=body)

    print(response)
