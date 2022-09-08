"""
Delete a tag filtering entry returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_namespace import AWSNamespace
from datadog_api_client.v1.model.aws_tag_filter_delete_request import AWSTagFilterDeleteRequest

body = AWSTagFilterDeleteRequest(
    account_id="FAKEAC0FAKEAC2FAKEAC",
    namespace=AWSNamespace.ELB,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.delete_aws_tag_filter(body=body)

    print(response)
