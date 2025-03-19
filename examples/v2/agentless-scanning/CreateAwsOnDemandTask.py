"""
Post an AWS on demand task returns "AWS on demand task created successfully." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.agentless_scanning_api import AgentlessScanningApi
from datadog_api_client.v2.model.aws_on_demand_create_attributes import AwsOnDemandCreateAttributes
from datadog_api_client.v2.model.aws_on_demand_create_data import AwsOnDemandCreateData
from datadog_api_client.v2.model.aws_on_demand_create_request import AwsOnDemandCreateRequest
from datadog_api_client.v2.model.aws_on_demand_type import AwsOnDemandType

body = AwsOnDemandCreateRequest(
    data=AwsOnDemandCreateData(
        attributes=AwsOnDemandCreateAttributes(
            arn="arn:aws:lambda:eu-west-3:376334461865:function:This-Is-An-Api-Spec-Test",
        ),
        type=AwsOnDemandType.AWS_RESOURCE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AgentlessScanningApi(api_client)
    response = api_instance.create_aws_on_demand_task(body=body)

    print(response)
