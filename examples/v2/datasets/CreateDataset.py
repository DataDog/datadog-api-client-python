"""
Create a dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi
from datadog_api_client.v2.model.dataset_attributes_request import DatasetAttributesRequest
from datadog_api_client.v2.model.dataset_create_request import DatasetCreateRequest
from datadog_api_client.v2.model.dataset_request import DatasetRequest
from datadog_api_client.v2.model.dataset_type import DatasetType
from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

body = DatasetCreateRequest(
    data=DatasetRequest(
        attributes=DatasetAttributesRequest(
            name="Security Audit Dataset",
            principals=[
                "role:94172442-be03-11e9-a77a-3b7612558ac1",
            ],
            product_filters=[
                FiltersPerProduct(
                    filters=[
                        "@application.id:ABCD",
                    ],
                    product="metrics",
                ),
            ],
        ),
        type=DatasetType.DATASET,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_dataset"] = True
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.create_dataset(body=body)

    print(response)
