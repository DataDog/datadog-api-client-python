"""
Get the details of an error tracking issue returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.get_issue(
        issue_id=ISSUE_ID,
    )

    print(response)
