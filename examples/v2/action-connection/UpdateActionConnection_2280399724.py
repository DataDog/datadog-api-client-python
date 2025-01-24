"""
Update an existing Action Connection returns "Successfully updated Action Connection" response
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
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributesUpdate(
            name="Cassette Connection",
            integration=AWSIntegrationUpdate(
                type=AWSIntegrationType.AWS,
                credentials=AWSAssumeRoleUpdate(
                    type=AWSAssumeRoleType.AWSASSUMEROLE,
                    role="MyRoleUpdated",
                    account_id="123456789123",
                ),
            ),
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.update_action_connection(connection_id="cb460d51-3c88-4e87-adac-d47131d0423d", body=body)

    print(response)
