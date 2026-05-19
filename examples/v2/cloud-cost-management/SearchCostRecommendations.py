"""
Search cost recommendations returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.recommendations_filter_request import RecommendationsFilterRequest
from datadog_api_client.v2.model.recommendations_filter_request_sort_items import RecommendationsFilterRequestSortItems

body = RecommendationsFilterRequest(
    filter="@resource_table:aws_ec2_instance",
    sort=[
        RecommendationsFilterRequestSortItems(
            expression="potential_daily_savings.amount",
            order="DESC",
        ),
    ],
)

configuration = Configuration()
configuration.unstable_operations["search_cost_recommendations"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.search_cost_recommendations(body=body)

    print(response)
