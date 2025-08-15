"""
Delete datastore returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.actions_datastores_api import ActionsDatastoresApi

# a "datastore" is created in the system
CREATED_DATASTORE_DATA_ID = environ["CREATED_DATASTORE_DATA_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ActionsDatastoresApi(api_client)
    api_instance.delete_datastore(
        datastore_id=CREATED_DATASTORE_DATA_ID,
    )
