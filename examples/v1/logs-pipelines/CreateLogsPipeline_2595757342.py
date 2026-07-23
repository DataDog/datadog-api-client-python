"""
Create a pipeline with Array Processor Key Value Operation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_extract_key_value import (
    LogsArrayProcessorOperationExtractKeyValue,
)
from datadog_api_client.v1.model.logs_array_processor_operation_extract_key_value_type import (
    LogsArrayProcessorOperationExtractKeyValueType,
)
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayKeyValue",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="extract_kv",
            operation=LogsArrayProcessorOperationExtractKeyValue(
                type=LogsArrayProcessorOperationExtractKeyValueType.KEY_VALUE,
                source="tags",
                key_to_extract="name",
                value_to_extract="value",
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
