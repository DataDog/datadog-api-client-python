"""
Create a pipeline with Array Processor Length Operation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_length import LogsArrayProcessorOperationLength
from datadog_api_client.v1.model.logs_array_processor_operation_length_type import LogsArrayProcessorOperationLengthType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayLength",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="count_tags",
            operation=LogsArrayProcessorOperationLength(
                type=LogsArrayProcessorOperationLengthType.LENGTH,
                source="tags",
                target="tagCount",
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
