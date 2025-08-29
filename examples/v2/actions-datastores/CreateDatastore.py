"""
Create datastore returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.create_apps_datastore_request import CreateAppsDatastoreRequest
from datadog_api_client.v2.model.create_apps_datastore_request_data import CreateAppsDatastoreRequestData
from datadog_api_client.v2.model.create_apps_datastore_request_data_attributes import (
    CreateAppsDatastoreRequestDataAttributes,
)
from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType

body = CreateAppsDatastoreRequest(
    data=CreateAppsDatastoreRequestData(
        attributes=CreateAppsDatastoreRequestDataAttributes(
            name="datastore-name",
            primary_column_name="primaryKey",
        ),
        type=DatastoreDataType.DATASTORES,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.create_datastore(body=body)

    print(response)
