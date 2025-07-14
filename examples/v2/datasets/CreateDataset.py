"""
Create a dataset returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.datasets_api import DatasetsApi
from datadog_api_client.v2.model.dataset import Dataset
from datadog_api_client.v2.model.dataset_attributes import DatasetAttributes
from datadog_api_client.v2.model.dataset_create_request import DatasetCreateRequest
from datadog_api_client.v2.model.filters_per_product import FiltersPerProduct

body = DatasetCreateRequest(
    data=Dataset(
        attributes=DatasetAttributes(
            created_at=None,
            name="Security Audit Dataset",
            principals=[
                "role:86245fce-0a4e-11f0-92bd-da7ad0900002",
            ],
            product_filters=[
                FiltersPerProduct(
                    filters=[
                        "@application.id:ABCD",
                    ],
                    product="logs",
                ),
            ],
        ),
        id="123e4567-e89b-12d3-a456-426614174000",
        type="dataset",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DatasetsApi(api_client)
    response = api_instance.create_dataset(body=body)

    print(response)
