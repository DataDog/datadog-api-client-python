"""
Update a specific Org Config returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi
from datadog_api_client.v2.model.org_config_type import OrgConfigType
from datadog_api_client.v2.model.org_config_write import OrgConfigWrite
from datadog_api_client.v2.model.org_config_write_attributes import OrgConfigWriteAttributes
from datadog_api_client.v2.model.org_config_write_request import OrgConfigWriteRequest

body = OrgConfigWriteRequest(
    data=OrgConfigWrite(
        attributes=OrgConfigWriteAttributes(
            value="UTC",
        ),
        type=OrgConfigType.ORG_CONFIGS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    response = api_instance.update_org_config(org_config_name="monitor_timezone", body=body)

    print(response)
