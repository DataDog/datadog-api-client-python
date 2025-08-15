"""
Put datastore item returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.put_apps_datastore_item_request import PutAppsDatastoreItemRequest
from datadog_api_client.v2.model.put_apps_datastore_item_request_data import PutAppsDatastoreItemRequestData
from datadog_api_client.v2.model.put_apps_datastore_item_request_data_attributes import (
    PutAppsDatastoreItemRequestDataAttributes,
)
from datadog_api_client.v2.model.put_apps_datastore_item_request_data_type import PutAppsDatastoreItemRequestDataType

# there is a valid "datastore" in the system
DATASTORE_DATA_ATTRIBUTES_PRIMARY_COLUMN_NAME = environ["DATASTORE_DATA_ATTRIBUTES_PRIMARY_COLUMN_NAME"]
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = PutAppsDatastoreItemRequest(
    data=PutAppsDatastoreItemRequestData(
        attributes=PutAppsDatastoreItemRequestDataAttributes(
            value=dict(
                [("28173b88-1a0e-001e-28c0-7664b6410518", "new-item-key"), ("data", "example data"), ("key", "value")]
            ),
        ),
        type=PutAppsDatastoreItemRequestDataType.ITEMS,
        id="e7e64418-b60c-4789-9612-895ac8423207",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.put_datastore_item(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)
