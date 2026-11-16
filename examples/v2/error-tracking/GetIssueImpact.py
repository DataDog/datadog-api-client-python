"""
Get the impact of an error tracking issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["get_issue_impact"] = True
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.get_issue_impact(
        issue_id=ISSUE_ID,
        filter_from=1635333071000,
        filter_to=1636629071000,
    )

    print(response)
