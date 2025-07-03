"""
Create a pipeline with Array Processor Append Operation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_append import LogsArrayProcessorOperationAppend
from datadog_api_client.v1.model.logs_array_processor_operation_append_type import LogsArrayProcessorOperationAppendType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayAppend",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="append_ip_to_array",
            operation=LogsArrayProcessorOperationAppend(
                type=LogsArrayProcessorOperationAppendType.APPEND,
                source="network.client.ip",
                target="sourceIps",
            ),
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)
