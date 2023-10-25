"""
Create an Amazon EventBridge source returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v1.model.aws_event_bridge_create_request import AWSEventBridgeCreateRequest

body = AWSEventBridgeCreateRequest(
    account_id="123456789012",
    create_event_bus=True,
    event_generator_name="app-alerts",
    region="us-east-1",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.create_aws_event_bridge_source(body=body)

    print(response)
