"""
Edit a dataset returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi
from datadog_api_client.v2.model.dataset_attributes_request import DatasetAttributesRequest
from datadog_api_client.v2.model.dataset_request import DatasetRequest
from datadog_api_client.v2.model.dataset_type import DatasetType
from datadog_api_client.v2.model.dataset_update_request import DatasetUpdateRequest
from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

# there is a valid "dataset" in the system
DATASET_DATA_ID = environ["DATASET_DATA_ID"]

body = DatasetUpdateRequest(
    data=DatasetRequest(
        attributes=DatasetAttributesRequest(
            name="Security Audit Dataset",
            principals=[
                "role:94172442-be03-11e9-a77a-3b7612558ac1",
            ],
            product_filters=[
                FiltersPerProduct(
                    filters=[
                        "@application.id:1234",
                    ],
                    product="metrics",
                ),
            ],
        ),
        type=DatasetType.DATASET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.update_dataset(dataset_id=DATASET_DATA_ID, body=body)

    print(response)
