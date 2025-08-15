"""
Create datastore from import returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.create_apps_datastore_from_import_request import CreateAppsDatastoreFromImportRequest
from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data import (
    CreateAppsDatastoreFromImportRequestData,
)
from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data_attributes import (
    CreateAppsDatastoreFromImportRequestDataAttributes,
)
from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data_type import (
    CreateAppsDatastoreFromImportRequestDataType,
)

body = CreateAppsDatastoreFromImportRequest(
    data=CreateAppsDatastoreFromImportRequestData(
        attributes=CreateAppsDatastoreFromImportRequestDataAttributes(
            name="datastore-name",
            primary_column_name="primaryKey",
            values=[
                dict([("primaryKey", "key1"), ("value", "{'data': 'example data 1', 'key': 'value'}")]),
                dict([("primaryKey", "key2"), ("value", "{'data': 'example data 2', 'key': 'value'}")]),
            ],
        ),
        type=CreateAppsDatastoreFromImportRequestDataType.DATASTORES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.create_datastore_from_import(body=body)

    print(response)
