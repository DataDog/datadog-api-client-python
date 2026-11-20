"""
Order RUM retention filters returns "Ordered" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_retention_filters_api import RUMRetentionFiltersApi
from datadog_api_client.v2.model.rum_retention_filter_type import RUMRetentionFilterType
from datadog_api_client.v2.model.rum_retention_filters_order_data import RUMRetentionFiltersOrderData
from datadog_api_client.v2.model.rum_retention_filters_order_request import RUMRetentionFiltersOrderRequest

body = RUMRetentionFiltersOrderRequest(
    data=[
        RUMRetentionFiltersOrderData(
            type=RUMRetentionFilterType.RETENTION_FILTERS,
            id="325631eb-94c9-49c0-93f9-ab7e4fd24529",
        ),
        RUMRetentionFiltersOrderData(
            type=RUMRetentionFilterType.RETENTION_FILTERS,
            id="42d89430-5b80-426e-a44b-ba3b417ece25",
        ),
        RUMRetentionFiltersOrderData(
            type=RUMRetentionFilterType.RETENTION_FILTERS,
            id="bff0bc34-99e9-4c16-adce-f47e71948c23",
        ),
    ],
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = RUMRetentionFiltersApi(api_client)
    response = api_instance.order_retention_filters(app_id="1d4b9c34-7ac4-423a-91cf-9902d926e9b3", body=body)

    print(response)
