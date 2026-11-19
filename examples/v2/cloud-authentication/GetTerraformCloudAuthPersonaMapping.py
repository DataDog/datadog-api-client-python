"""
Get an HCP Terraform persona mapping returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi

# there is a valid "terraform_cloud_auth_persona_mapping" in the system
TERRAFORM_CLOUD_AUTH_PERSONA_MAPPING_DATA_ID = environ["TERRAFORM_CLOUD_AUTH_PERSONA_MAPPING_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_terraform_cloud_auth_persona_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.get_terraform_cloud_auth_persona_mapping(
        persona_mapping_id=TERRAFORM_CLOUD_AUTH_PERSONA_MAPPING_DATA_ID,
    )

    print(response)
