"""
Delete an Amazon EventBridge source returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_event_bridge_delete_request import AWSEventBridgeDeleteRequest

body = AWSEventBridgeDeleteRequest(
    account_id="123456789012",
    event_generator_name="app-alerts-zyxw3210",
    region="us-east-1",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.delete_aws_event_bridge_source(body=body)

    print(response)
