"""
Update a connection group returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.action_connection_api import ActionConnectionApi
from datadog_api_client.v2.model.connection_group_data_attributes_request import ConnectionGroupDataAttributesRequest
from datadog_api_client.v2.model.connection_group_data_request import ConnectionGroupDataRequest
from datadog_api_client.v2.model.connection_group_type import ConnectionGroupType
from datadog_api_client.v2.model.update_connection_group_request import UpdateConnectionGroupRequest

body = UpdateConnectionGroupRequest(
    data=ConnectionGroupDataRequest(
        attributes=ConnectionGroupDataAttributesRequest(
            connections=[],
            description="An updated test connection group for AWS integrations",
            name="My Connection Group Updated",
            tag_keys=[],
        ),
        type=ConnectionGroupType.CONNECTION_GROUP,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_connection_group"] = True
with ApiClient(configuration) as api_client:
    api_instance = ActionConnectionApi(api_client)
    response = api_instance.update_connection_group(connection_group_id="connection_group_id", body=body)

    print(response)
