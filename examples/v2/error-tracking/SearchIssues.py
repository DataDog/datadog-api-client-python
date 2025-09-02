"""
Search error tracking issues returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.error_tracking_api import ErrorTrackingApi
from datadog_api_client.v2.model.issues_search_request import IssuesSearchRequest
from datadog_api_client.v2.model.issues_search_request_data import IssuesSearchRequestData
from datadog_api_client.v2.model.issues_search_request_data_attributes import IssuesSearchRequestDataAttributes
from datadog_api_client.v2.model.issues_search_request_data_attributes_track import (
    IssuesSearchRequestDataAttributesTrack,
)
from datadog_api_client.v2.model.issues_search_request_data_type import IssuesSearchRequestDataType

body = IssuesSearchRequest(
    data=IssuesSearchRequestData(
        attributes=IssuesSearchRequestDataAttributes(
            query="service:orders-* AND @language:go",
            _from=1671612804000,
            to=1671620004000,
            track=IssuesSearchRequestDataAttributesTrack.TRACE,
        ),
        type=IssuesSearchRequestDataType.SEARCH_REQUEST,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ErrorTrackingApi(api_client)
    response = api_instance.search_issues(body=body)

    print(response)
