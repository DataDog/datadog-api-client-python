"""
Create an AWS WIF intake mapping returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.awswif_api import AWSWIFApi
from datadog_api_client.v2.model.aws_wif_intake_mapping_attributes import AwsWifIntakeMappingAttributes
from datadog_api_client.v2.model.aws_wif_intake_mapping_create_data import AwsWifIntakeMappingCreateData
from datadog_api_client.v2.model.aws_wif_intake_mapping_create_request import AwsWifIntakeMappingCreateRequest
from datadog_api_client.v2.model.aws_wif_intake_mapping_type import AwsWifIntakeMappingType

body = AwsWifIntakeMappingCreateRequest(
    data=AwsWifIntakeMappingCreateData(
        attributes=AwsWifIntakeMappingAttributes(
            arn_pattern="arn:aws:iam::123456789012:role/my-agent-role",
        ),
        type=AwsWifIntakeMappingType.AWS_WIF_INTAKE_MAPPING,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSWIFApi(api_client)
    response = api_instance.create_aws_wif_intake_mapping(body=body)

    print(response)
