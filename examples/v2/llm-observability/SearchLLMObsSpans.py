"""
Search LLM Observability spans returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_search_spans_request import LLMObsSearchSpansRequest
from datadog_api_client.v2.model.llm_obs_search_spans_request_attributes import LLMObsSearchSpansRequestAttributes
from datadog_api_client.v2.model.llm_obs_search_spans_request_data import LLMObsSearchSpansRequestData
from datadog_api_client.v2.model.llm_obs_search_spans_request_type import LLMObsSearchSpansRequestType
from datadog_api_client.v2.model.llm_obs_span_filter import LLMObsSpanFilter
from datadog_api_client.v2.model.llm_obs_span_page_query import LLMObsSpanPageQuery
from datadog_api_client.v2.model.llm_obs_span_search_options import LLMObsSpanSearchOptions

body = LLMObsSearchSpansRequest(
    data=LLMObsSearchSpansRequestData(
        attributes=LLMObsSearchSpansRequestAttributes(
            filter=LLMObsSpanFilter(
                _from="now-900s",
                ml_app="my-llm-app",
                query="@session_id:abc123def456",
                span_id="abc123def456",
                span_kind="llm",
                span_name="llm_call",
                to="now",
                trace_id="trace-9a8b7c6d5e4f",
            ),
            options=LLMObsSpanSearchOptions(
                include_attachments=True,
                time_offset=0,
            ),
            page=LLMObsSpanPageQuery(
                cursor="eyJzdGFydCI6MTAwfQ==",
                limit=10,
            ),
            sort="-start_ns",
        ),
        type=LLMObsSearchSpansRequestType.SPANS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["search_llm_obs_spans"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.search_llm_obs_spans(body=body)

    print(response)
