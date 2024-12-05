"""
Creates a data deletion request returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.data_deletion_api import DataDeletionApi
from datadog_api_client.v2.model.create_data_deletion_request_body import CreateDataDeletionRequestBody
from datadog_api_client.v2.model.create_data_deletion_request_body_attributes import (
    CreateDataDeletionRequestBodyAttributes,
)
from datadog_api_client.v2.model.create_data_deletion_request_body_data import CreateDataDeletionRequestBodyData

body = CreateDataDeletionRequestBody(
    data=CreateDataDeletionRequestBodyData(
        attributes=CreateDataDeletionRequestBodyAttributes(
            _from=1672527600000,
            indexes=[
                "test-index",
                "test-index-2",
            ],
            query=dict(
                host="abc",
                service="xyz",
            ),
            to=1704063600000,
        ),
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DataDeletionApi(api_client)
    response = api_instance.create_data_deletion_request(product="logs", body=body)

    print(response)
