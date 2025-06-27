"""
Create a pipeline with Array Processor Select Operation returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_processor import LogsArrayProcessor
from datadog_api_client.v1.model.logs_array_processor_operation_select import LogsArrayProcessorOperationSelect
from datadog_api_client.v1.model.logs_array_processor_operation_select_type import LogsArrayProcessorOperationSelectType
from datadog_api_client.v1.model.logs_array_processor_type import LogsArrayProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArraySelect",
    processors=[
        LogsArrayProcessor(
            type=LogsArrayProcessorType.ARRAY_PROCESSOR,
            is_enabled=True,
            name="extract_referrer",
            operation=LogsArrayProcessorOperationSelect(
                type=LogsArrayProcessorOperationSelectType.SELECT,
                source="httpRequest.headers",
                target="referrer",
                filter="name:Referrer",
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
