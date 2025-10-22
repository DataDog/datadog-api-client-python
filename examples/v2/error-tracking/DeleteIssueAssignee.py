"""
Remove the assignee of an issue returns "No Content" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    api_instance.delete_issue_assignee(
        issue_id=ISSUE_ID,
    )
