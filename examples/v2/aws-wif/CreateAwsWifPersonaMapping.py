"""
Create an AWS WIF persona mapping returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.awswif_api import AWSWIFApi
from datadog_api_client.v2.model.aws_wif_persona_mapping_create_attributes import AwsWifPersonaMappingCreateAttributes
from datadog_api_client.v2.model.aws_wif_persona_mapping_create_data import AwsWifPersonaMappingCreateData
from datadog_api_client.v2.model.aws_wif_persona_mapping_create_request import AwsWifPersonaMappingCreateRequest
from datadog_api_client.v2.model.aws_wif_persona_mapping_type import AwsWifPersonaMappingType

body = AwsWifPersonaMappingCreateRequest(
    data=AwsWifPersonaMappingCreateData(
        attributes=AwsWifPersonaMappingCreateAttributes(
            account_identifier="user@example.com",
            arn_pattern="arn:aws:iam::123456789012:role/my-workload-role",
        ),
        type=AwsWifPersonaMappingType.AWS_WIF_CONFIG,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSWIFApi(api_client)
    response = api_instance.create_aws_wif_persona_mapping(body=body)

    print(response)
