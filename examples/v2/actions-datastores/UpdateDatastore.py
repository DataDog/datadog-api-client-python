"""
Update datastore returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi
from datadog_api_client.v2.model.datastore_data_type import DatastoreDataType
from datadog_api_client.v2.model.update_apps_datastore_request import UpdateAppsDatastoreRequest
from datadog_api_client.v2.model.update_apps_datastore_request_data import UpdateAppsDatastoreRequestData
from datadog_api_client.v2.model.update_apps_datastore_request_data_attributes import (
    UpdateAppsDatastoreRequestDataAttributes,
)

# there is a valid "datastore" in the system
DATASTORE_DATA_ID = environ["DATASTORE_DATA_ID"]

body = UpdateAppsDatastoreRequest(
    data=UpdateAppsDatastoreRequestData(
        attributes=UpdateAppsDatastoreRequestDataAttributes(
            name="updated name",
        ),
        type=DatastoreDataType.DATASTORES,
        id=DATASTORE_DATA_ID,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    response = api_instance.update_datastore(datastore_id=DATASTORE_DATA_ID, body=body)

    print(response)
