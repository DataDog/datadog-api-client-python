"""
Bulk delete datastore items returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request import BulkDeleteAppsDatastoreItemsRequest
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data import (
    BulkDeleteAppsDatastoreItemsRequestData,
)
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data_attributes import (
    BulkDeleteAppsDatastoreItemsRequestDataAttributes,
)
from datadog_api_client.v2.model.bulk_delete_apps_datastore_items_request_data_type import (
    BulkDeleteAppsDatastoreItemsRequestDataType,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = BulkDeleteAppsDatastoreItemsRequest(
    data=BulkDeleteAppsDatastoreItemsRequestData(
        attributes=BulkDeleteAppsDatastoreItemsRequestDataAttributes(
            item_keys=[
                "test-key",
            ],
        ),
        type=BulkDeleteAppsDatastoreItemsRequestDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.bulk_delete_datastore_items(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)
