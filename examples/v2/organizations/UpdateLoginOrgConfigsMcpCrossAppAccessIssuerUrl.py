"""
Update the MCP Cross-App Access issuer URL returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.organizations_api import OrganizationsApi
from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_type import McpCrossAppAccessIssuerUrlType
from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_update_attributes import (
    McpCrossAppAccessIssuerUrlUpdateAttributes,
)
from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_update_data import McpCrossAppAccessIssuerUrlUpdateData
from datadog_api_client.v2.model.mcp_cross_app_access_issuer_url_update_request import (
    McpCrossAppAccessIssuerUrlUpdateRequest,
)

body = McpCrossAppAccessIssuerUrlUpdateRequest(
    data=McpCrossAppAccessIssuerUrlUpdateData(
        attributes=McpCrossAppAccessIssuerUrlUpdateAttributes(
            issuer_url="https://your-subdomain.okta.com",
        ),
        type=McpCrossAppAccessIssuerUrlType.ORG_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_login_org_configs_mcp_cross_app_access_issuer_url"] = True
with ApiClient(configuration) as api_client:
    api_instance = OrganizationsApi(api_client)
    api_instance.update_login_org_configs_mcp_cross_app_access_issuer_url(body=body)
