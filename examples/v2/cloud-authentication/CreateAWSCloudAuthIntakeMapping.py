"""
Create an AWS cloud authentication intake mapping returns "Created" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi
from datadog_api_client.v2.model.aws_cloud_auth_intake_mapping_create_attributes import (
    AWSCloudAuthIntakeMappingCreateAttributes,
)
from datadog_api_client.v2.model.aws_cloud_auth_intake_mapping_create_data import AWSCloudAuthIntakeMappingCreateData
from datadog_api_client.v2.model.aws_cloud_auth_intake_mapping_create_request import (
    AWSCloudAuthIntakeMappingCreateRequest,
)
from datadog_api_client.v2.model.aws_cloud_auth_intake_mapping_type import AWSCloudAuthIntakeMappingType

# there is an integrated AWS test account for WIF
AWS_WIF_ACCOUNT_V2_DATA_0_ATTRIBUTES_AWS_ACCOUNT_ID = environ["AWS_WIF_ACCOUNT_V2_DATA_0_ATTRIBUTES_AWS_ACCOUNT_ID"]

body = AWSCloudAuthIntakeMappingCreateRequest(
    data=AWSCloudAuthIntakeMappingCreateData(
        type=AWSCloudAuthIntakeMappingType.AWS_CLOUD_AUTH_INTAKE_MAPPING,
        attributes=AWSCloudAuthIntakeMappingCreateAttributes(
            arn_pattern="arn:aws:sts::123456789012:assumed-role/DatadogAgent-de20b7e944abfac3/*",
        ),
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["create_aws_cloud_auth_intake_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.create_aws_cloud_auth_intake_mapping(body=body)

    print(response)
