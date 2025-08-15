"""
Bulk put datastore items returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request import BulkPutAppsDatastoreItemsRequest
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data import BulkPutAppsDatastoreItemsRequestData
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data_attributes import (
    BulkPutAppsDatastoreItemsRequestDataAttributes,
)
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data_type import (
    BulkPutAppsDatastoreItemsRequestDataType,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ATTRIBUTES_PRIMARY_COLUMN_NAME = environ["DATASTORE_DATA_ATTRIBUTES_PRIMARY_COLUMN_NAME"]
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = BulkPutAppsDatastoreItemsRequest(
    data=BulkPutAppsDatastoreItemsRequestData(
        attributes=BulkPutAppsDatastoreItemsRequestDataAttributes(
            values=[
                dict(
                    [
                        ("28173b88-1a0e-001e-28c0-7664b6410518", "key1"),
                        ("value", "{'data': 'example data 1', 'key': 'value'}"),
                    ]
                ),
                dict(
                    [
                        ("28173b88-1a0e-001e-28c0-7664b6410518", "key2"),
                        ("value", "{'data': 'example data 2', 'key': 'value'}"),
                    ]
                ),
            ],
        ),
        type=BulkPutAppsDatastoreItemsRequestDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.bulk_put_datastore_items(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)
