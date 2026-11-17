"""
Get funnel step suggestions returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.product_analytics_api import ProductAnalyticsApi
from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_request import (
    ProductAnalyticsFunnelStepSuggestionsRequest,
)
from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_request_attributes import (
    ProductAnalyticsFunnelStepSuggestionsRequestAttributes,
)
from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_request_data import (
    ProductAnalyticsFunnelStepSuggestionsRequestData,
)
from datadog_api_client.v2.model.product_analytics_funnel_step_suggestions_request_type import (
    ProductAnalyticsFunnelStepSuggestionsRequestType,
)

body = ProductAnalyticsFunnelStepSuggestionsRequest(
    data=ProductAnalyticsFunnelStepSuggestionsRequestData(
        attributes=ProductAnalyticsFunnelStepSuggestionsRequestAttributes(
            application_id="40d8ca4b-2ac0-481f-b16e-f110699ecff6",
            expression="node_01->node_02",
            steps=dict(
                node_01="@type:view @view.name:/checkout",
                node_02="@type:action @action.name:pay",
            ),
        ),
        type=ProductAnalyticsFunnelStepSuggestionsRequestType.FUNNEL_SUGGESTIONS_STEPS_REQUEST,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["query_product_analytics_funnel_step_suggestions"] = True
with ApiClient(configuration) as api_client:
    api_instance = ProductAnalyticsApi(api_client)
    response = api_instance.query_product_analytics_funnel_step_suggestions(body=body)

    print(response)
