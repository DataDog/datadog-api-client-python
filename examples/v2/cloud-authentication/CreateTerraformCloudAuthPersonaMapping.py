"""
Create an HCP Terraform persona mapping returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi
from datadog_api_client.v2.model.terraform_cloud_auth_issuer_url import TerraformCloudAuthIssuerURL
from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_create_attributes import (
    TerraformCloudAuthPersonaMappingCreateAttributes,
)
from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_create_data import (
    TerraformCloudAuthPersonaMappingCreateData,
)
from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_create_request import (
    TerraformCloudAuthPersonaMappingCreateRequest,
)
from datadog_api_client.v2.model.terraform_cloud_auth_persona_mapping_type import TerraformCloudAuthPersonaMappingType

# there is a valid "service_account_user_with_role" in the system
SERVICE_ACCOUNT_USER_WITH_ROLE_DATA_ATTRIBUTES_EMAIL = environ["SERVICE_ACCOUNT_USER_WITH_ROLE_DATA_ATTRIBUTES_EMAIL"]

body = TerraformCloudAuthPersonaMappingCreateRequest(
    data=TerraformCloudAuthPersonaMappingCreateData(
        type=TerraformCloudAuthPersonaMappingType.TERRAFORM_CLOUD_AUTH_CONFIG,
        attributes=TerraformCloudAuthPersonaMappingCreateAttributes(
            issuer_url=TerraformCloudAuthIssuerURL.US,
            sub_pattern="organization:datadog-api-spec:project:Default Project:workspace:sdk-examplecloudauthentication:run_phase:*",
            account_identifier=SERVICE_ACCOUNT_USER_WITH_ROLE_DATA_ATTRIBUTES_EMAIL,
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_terraform_cloud_auth_persona_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.create_terraform_cloud_auth_persona_mapping(body=body)

    print(response)
