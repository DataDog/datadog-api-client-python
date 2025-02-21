"""
Create a pipeline with Span Id Remapper returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline
from datadog_api_client.v1.model.logs_span_remapper import LogsSpanRemapper
from datadog_api_client.v1.model.logs_span_remapper_type import LogsSpanRemapperType

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipeline",
    processors=[
        LogsSpanRemapper(
            type=LogsSpanRemapperType.SPAN_ID_REMAPPER,
            is_enabled=True,
            name="test_filter",
            sources=[
                "dd.span_id",
            ],
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)
