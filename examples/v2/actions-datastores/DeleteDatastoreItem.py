"""
Delete datastore item returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType
from datadog_api_client.v2.model.delete_apps_datastore_item_request import DeleteAppsDatastoreItemRequest
from datadog_api_client.v2.model.delete_apps_datastore_item_request_data import DeleteAppsDatastoreItemRequestData
from datadog_api_client.v2.model.delete_apps_datastore_item_request_data_attributes import (
    DeleteAppsDatastoreItemRequestDataAttributes,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = DeleteAppsDatastoreItemRequest(
    data=DeleteAppsDatastoreItemRequestData(
        attributes=DeleteAppsDatastoreItemRequestDataAttributes(
            item_key="test-key",
        ),
        type=DatastoreItemsDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.delete_datastore_item(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)
