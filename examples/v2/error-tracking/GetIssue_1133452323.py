"""
Get the details of an error tracking issue with samples returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi
from datadog_api_client.v2.model.get_issue_include_query_parameter_item import GetIssueIncludeQueryParameterItem
from datadog_api_client.v2.model.issue_sample_bias import IssueSampleBias

# there is a valid "issue" in the system
ISSUE_ID = environ["ISSUE_ID"]

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.get_issue(
        issue_id=ISSUE_ID,
        include=[
            GetIssueIncludeQueryParameterItem.SAMPLES,
        ],
        filter_samples_biases=[
            IssueSampleBias.LATEST,
        ],
    )

    print(response)
