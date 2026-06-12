"""
Create a pipeline with Array Map Processor using arithmetic sub-processor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_arithmetic_processor import LogsArithmeticProcessor
from datadog_api_client.v1.model.logs_arithmetic_processor_type import LogsArithmeticProcessorType
from datadog_api_client.v1.model.logs_array_map_processor import LogsArrayMapProcessor
from datadog_api_client.v1.model.logs_array_map_processor_type import LogsArrayMapProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayMapArithmetic",
    processors=[
        LogsArrayMapProcessor(
            type=LogsArrayMapProcessorType.ARRAY_MAP_PROCESSOR,
            is_enabled=True,
            name="double counts",
            source="items",
            target="out",
            processors=[
                LogsArithmeticProcessor(
                    type=LogsArithmeticProcessorType.ARITHMETIC_PROCESSOR,
                    expression="$sourceElem.count * 2",
                    target="$targetElem.doubled",
                ),
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
