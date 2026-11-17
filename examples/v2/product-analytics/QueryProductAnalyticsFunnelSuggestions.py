"""
Get feature suggestions returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_funnel_suggestions_request import (
    ProductAnalyticsFunnelSuggestionsRequest,
)
from datadog_api_client.v2.model.product_analytics_funnel_suggestions_request_attributes import (
    ProductAnalyticsFunnelSuggestionsRequestAttributes,
)
from datadog_api_client.v2.model.product_analytics_funnel_suggestions_request_data import (
    ProductAnalyticsFunnelSuggestionsRequestData,
)
from datadog_api_client.v2.model.product_analytics_funnel_suggestions_request_type import (
    ProductAnalyticsFunnelSuggestionsRequestType,
)

body = ProductAnalyticsFunnelSuggestionsRequest(
    data=ProductAnalyticsFunnelSuggestionsRequestData(
        attributes=ProductAnalyticsFunnelSuggestionsRequestAttributes(
            application_id="40d8ca4b-2ac0-481f-b16e-f110699ecff6",
        ),
        type=ProductAnalyticsFunnelSuggestionsRequestType.FUNNEL_SUGGESTIONS_REQUEST,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["query_product_analytics_funnel_suggestions"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.query_product_analytics_funnel_suggestions(body=body)

    print(response)
