"""
Delete a cost recommendation notification rule returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["delete_cost_recommendation_notification_rule"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    api_instance.delete_cost_recommendation_notification_rule(
        notification_rule_id="notification_rule_id",
    )
