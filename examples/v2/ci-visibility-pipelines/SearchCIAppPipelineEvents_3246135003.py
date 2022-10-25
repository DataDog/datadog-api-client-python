"""
Search pipelines events returns "OK" response with pagination
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.ci_visibility_pipelines_api import CIVisibilityPipelinesApi
from datadog_api_client.v2.model.ci_app_pipeline_events_request import CIAppPipelineEventsRequest
from datadog_api_client.v2.model.ci_app_pipelines_query_filter import CIAppPipelinesQueryFilter
from datadog_api_client.v2.model.ci_app_query_options import CIAppQueryOptions
from datadog_api_client.v2.model.ci_app_query_page_options import CIAppQueryPageOptions
from datadog_api_client.v2.model.ci_app_sort import CIAppSort

body = CIAppPipelineEventsRequest(
    filter=CIAppPipelinesQueryFilter(
        _from="now-30s",
        to="now",
    ),
    options=CIAppQueryOptions(
        timezone="GMT",
    ),
    page=CIAppQueryPageOptions(
        limit=2,
    ),
    sort=CIAppSort.TIMESTAMP_ASCENDING,
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = CIVisibilityPipelinesApi(api_client)
    items = api_instance.search_ci_app_pipeline_events_with_pagination(body=body)
    for item in items:
        print(item)
