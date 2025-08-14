"""
Update an existing Action Connection with HTTPBasicAuth returns "Successfully updated Action Connection" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.action_connection_attributes_update import ActionConnectionAttributesUpdate
from datadog_api_client.v2.model.action_connection_data_type import ActionConnectionDataType
from datadog_api_client.v2.model.action_connection_data_update import ActionConnectionDataUpdate
from datadog_api_client.v2.model.http_basic_auth_type import HTTPBasicAuthType
from datadog_api_client.v2.model.http_basic_auth_update import HTTPBasicAuthUpdate
from datadog_api_client.v2.model.http_integration_type import HTTPIntegrationType
from datadog_api_client.v2.model.http_integration_update import HTTPIntegrationUpdate
from datadog_api_client.v2.model.update_action_connection_request import UpdateActionConnectionRequest

body = UpdateActionConnectionRequest(
    data=ActionConnectionDataUpdate(
        type=ActionConnectionDataType.ACTION_CONNECTION,
        attributes=ActionConnectionAttributesUpdate(
            name="HTTP Basic Auth Updated",
            integration=HTTPIntegrationUpdate(
                type=HTTPIntegrationType.HTTP,
                base_url="https://api.updated.com",
                credentials=HTTPBasicAuthUpdate(
                    type=HTTPBasicAuthType.HTTPBASICAUTH,
                    username="updated-user",
                    password="updated-password",
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
