"""
Bulk write datastore items returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request import BulkPutAppsDatastoreItemsRequest
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data import BulkPutAppsDatastoreItemsRequestData
from datadog_api_client.v2.model.bulk_put_apps_datastore_items_request_data_attributes import (
    BulkPutAppsDatastoreItemsRequestDataAttributes,
)
from datadog_api_client.v2.model.datastore_items_data_type import DatastoreItemsDataType

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = BulkPutAppsDatastoreItemsRequest(
    data=BulkPutAppsDatastoreItemsRequestData(
        attributes=BulkPutAppsDatastoreItemsRequestDataAttributes(
            values=[
                dict([("id", "cust_3141"), ("name", "Johnathan")]),
                dict([("id", "cust_3142"), ("name", "Mary")]),
            ],
        ),
        type=DatastoreItemsDataType.ITEMS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.bulk_write_datastore_items(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)
