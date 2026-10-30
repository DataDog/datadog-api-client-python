"""
Delete an AWS cloud authentication intake mapping returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi

# there is a valid "aws_cloud_auth_intake_mapping" in the system
AWS_CLOUD_AUTH_INTAKE_MAPPING_DATA_ID = environ["AWS_CLOUD_AUTH_INTAKE_MAPPING_DATA_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_aws_cloud_auth_intake_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    api_instance.delete_aws_cloud_auth_intake_mapping(
        intake_mapping_id=AWS_CLOUD_AUTH_INTAKE_MAPPING_DATA_ID,
    )
