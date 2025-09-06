"""
Update datastore item returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.update_apps_datastore_item_request import UpdateAppsDatastoreItemRequest
from datadog_api_client.v2.model.update_apps_datastore_item_request_data import UpdateAppsDatastoreItemRequestData
from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes import (
    UpdateAppsDatastoreItemRequestDataAttributes,
)
from datadog_api_client.v2.model.update_apps_datastore_item_request_data_attributes_item_changes import (
    UpdateAppsDatastoreItemRequestDataAttributesItemChanges,
)
from datadog_api_client.v2.model.update_apps_datastore_item_request_data_type import (
    UpdateAppsDatastoreItemRequestDataType,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = UpdateAppsDatastoreItemRequest(
    data=UpdateAppsDatastoreItemRequestData(
        attributes=UpdateAppsDatastoreItemRequestDataAttributes(
            item_changes=UpdateAppsDatastoreItemRequestDataAttributesItemChanges(),
            item_key="test-key",
        ),
        type=UpdateAppsDatastoreItemRequestDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.update_datastore_item(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)
