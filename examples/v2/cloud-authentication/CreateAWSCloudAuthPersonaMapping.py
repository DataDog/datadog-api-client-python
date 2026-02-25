"""
Create an AWS cloud authentication persona mapping returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_authentication_api import CloudAuthenticationApi
from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_create_attributes import (
    AWSCloudAuthPersonaMappingCreateAttributes,
)
from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_create_data import AWSCloudAuthPersonaMappingCreateData
from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_create_request import (
    AWSCloudAuthPersonaMappingCreateRequest,
)
from datadog_api_client.v2.model.aws_cloud_auth_persona_mapping_type import AWSCloudAuthPersonaMappingType

body = AWSCloudAuthPersonaMappingCreateRequest(
    data=AWSCloudAuthPersonaMappingCreateData(
        attributes=AWSCloudAuthPersonaMappingCreateAttributes(
            account_identifier="test@test.com",
            arn_pattern="arn:aws:iam::123456789012:user/testuser",
        ),
        type=AWSCloudAuthPersonaMappingType.AWS_CLOUD_AUTH_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_aws_cloud_auth_persona_mapping"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudAuthenticationApi(api_client)
    response = api_instance.create_aws_cloud_auth_persona_mapping(body=body)

    print(response)
