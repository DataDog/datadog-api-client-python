"""
Delete datastore item returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.delete_apps_datastore_item_request import DeleteAppsDatastoreItemRequest
from datadog_api_client.v2.model.delete_apps_datastore_item_request_data import DeleteAppsDatastoreItemRequestData
from datadog_api_client.v2.model.delete_apps_datastore_item_request_data_attributes import (
    DeleteAppsDatastoreItemRequestDataAttributes,
)
from datadog_api_client.v2.model.delete_apps_datastore_item_request_data_type import (
    DeleteAppsDatastoreItemRequestDataType,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

# there are valid "datastore items" in the system
DATASTORE_ITEMS_DATA_0_ID = environ["DATASTORE_ITEMS_DATA_0_ID"]

body = DeleteAppsDatastoreItemRequest(
    data=DeleteAppsDatastoreItemRequestData(
        attributes=DeleteAppsDatastoreItemRequestDataAttributes(
            id=DATASTORE_ITEMS_DATA_0_ID,
            item_key="",
        ),
        type=DeleteAppsDatastoreItemRequestDataType.ITEMS,
        id=DATASTORE_DATA_ID,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    api_instance.delete_datastore_item(datastore_id=DATASTORE_DATA_ID, body=body)
