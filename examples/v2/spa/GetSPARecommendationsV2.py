"""
Get SPA recommendations v2 returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.spa_api import SpaApi
from datadog_api_client.v2.model.recommendation_v2_request_attributes import RecommendationV2RequestAttributes
from datadog_api_client.v2.model.recommendation_v2_request_body import RecommendationV2RequestBody
from datadog_api_client.v2.model.recommendation_v2_request_data import RecommendationV2RequestData
from datadog_api_client.v2.model.recommendation_v2_request_type import RecommendationV2RequestType

body = RecommendationV2RequestBody(
    data=RecommendationV2RequestData(
        attributes=RecommendationV2RequestAttributes(
            arguments=[
                "",
            ],
        ),
        type=RecommendationV2RequestType.RECOMMENDATION_V2_REQUEST,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_spa_recommendations_v2"] = True
with ApiClient(configuration) as api_client:
    api_instance = SpaApi(api_client)
    response = api_instance.get_spa_recommendations_v2(service="service", body=body)

    print(response)
