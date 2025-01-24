"""
Update an existing Action Connection returns "Successfully updated an Action Connection." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes_update import ActionConnectionAttributesUpdate
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.action_connection_data_update import ActionConnectionDataUpdate
from datadog_api_client.v2.model.aws_assume_role_type import AWSAssumeRoleType
from datadog_api_client.v2.model.aws_assume_role_update import AWSAssumeRoleUpdate
from datadog_api_client.v2.model.aws_integration_type import AWSIntegrationType
from datadog_api_client.v2.model.aws_integration_update import AWSIntegrationUpdate
from datadog_api_client.v2.model.update_action_connection_request import UpdateActionConnectionRequest

body = UpdateActionConnectionRequest(
    data=ActionConnectionDataUpdate(
        attributes=ActionConnectionAttributesUpdate(
            integration=AWSIntegrationUpdate(
                credentials=AWSAssumeRoleUpdate(
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
    response = api_instance.update_action_connection(connection_id="connection_id", body=body)

    print(response)
