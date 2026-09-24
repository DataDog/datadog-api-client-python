"""
Unwatch a case returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.case_management_api import CaseManagementApi

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = CaseManagementApi(api_client)
    api_instance.unwatch_case(
        case_id="case_id",
        user_uuid="user_uuid",
    )
