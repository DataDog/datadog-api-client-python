"""
Set an AWS tag filter returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_namespace import AWSNamespace
from datadog_api_client.v1.model.aws_tag_filter_create_request import AWSTagFilterCreateRequest

body = AWSTagFilterCreateRequest(
    account_id="1234567",
    namespace=AWSNamespace.ELB,
    tag_filter_str="prod*",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_tag_filter(body=body)

    print(response)
