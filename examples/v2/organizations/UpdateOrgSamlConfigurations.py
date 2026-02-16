"""
Update organization SAML preferences returns "No Content - The SAML preferences were successfully updated." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi
from datadog_api_client.v2.model.saml_configurations_update_attributes import SamlConfigurationsUpdateAttributes
from datadog_api_client.v2.model.saml_configurations_update_request import SamlConfigurationsUpdateRequest
from datadog_api_client.v2.model.saml_configurations_update_request_data import SamlConfigurationsUpdateRequestData
from datadog_api_client.v2.model.saml_configurations_update_request_data_type import (
    SamlConfigurationsUpdateRequestDataType,
)
from uuid import UUID

body = SamlConfigurationsUpdateRequest(
    data=SamlConfigurationsUpdateRequestData(
        attributes=SamlConfigurationsUpdateAttributes(
            default_role_uuids=[
                UUID("19fcc38b-b651-46a0-b463-1f8f56c6a862"),
            ],
            jit_domains=[
                "example1.com",
                "example2.com",
            ],
        ),
        type=SamlConfigurationsUpdateRequestDataType.SAML_PREFERENCES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_org_saml_configurations"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    api_instance.update_org_saml_configurations(body=body)
