"""
Create a new Action Connection returns "Successfully created an Action Connection." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes import ActionConnectionAttributes
from datadog_api_client.v2.model.action_connection_data import ActionConnectionData
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.aws_assume_role import AWSAssumeRole
from datadog_api_client.v2.model.aws_assume_role_type import AWSAssumeRoleType
from datadog_api_client.v2.model.aws_integration import AWSIntegration
from datadog_api_client.v2.model.aws_integration_type import AWSIntegrationType
from datadog_api_client.v2.model.create_action_connection_request import CreateActionConnectionRequest

body = CreateActionConnectionRequest(
    data=ActionConnectionData(
        attributes=ActionConnectionAttributes(
            integration=AWSIntegration(
                credentials=AWSAssumeRole(
                    account_id="111222333444",
                    role="my-role",
                    type=AWSAssumeRoleType.AWSASSUMEROLE,
                ),
                type=AWSIntegrationType.AWS,
            ),
            name="My AWS Connection",
        ),
        type=ActionConnectionDataType.ACTION_CONNECTION,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.create_action_connection(body=body)

    print(response)
