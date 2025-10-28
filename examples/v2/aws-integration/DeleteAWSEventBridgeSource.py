"""
Delete an Amazon EventBridge source returns "Amazon EventBridge source deleted." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.aws_integration_api import AWSIntegrationApi
from datadog_api_client.v2.model.aws_event_bridge_delete_request import AWSEventBridgeDeleteRequest
from datadog_api_client.v2.model.aws_event_bridge_delete_request_attributes import AWSEventBridgeDeleteRequestAttributes
from datadog_api_client.v2.model.aws_event_bridge_delete_request_data import AWSEventBridgeDeleteRequestData
from datadog_api_client.v2.model.aws_event_bridge_type import AWSEventBridgeType

body = AWSEventBridgeDeleteRequest(
    data=AWSEventBridgeDeleteRequestData(
        attributes=AWSEventBridgeDeleteRequestAttributes(
            account_id="123456789012",
            event_generator_name="app-alerts-zyxw3210",
            region="us-east-1",
        ),
        type=AWSEventBridgeType.EVENT_BRIDGE,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = AWSIntegrationApi(api_client)
    response = api_instance.delete_aws_event_bridge_source(body=body)

    print(response)
