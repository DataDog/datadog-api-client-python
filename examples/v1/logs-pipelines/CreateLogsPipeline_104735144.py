"""
Create a pipeline with Array Map Processor with preserve_source false returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_map_processor import LogsArrayMapProcessor
from datadog_api_client.v1.model.logs_array_map_processor_type import LogsArrayMapProcessorType
from datadog_api_client.v1.model.logs_attribute_remapper import LogsAttributeRemapper
from datadog_api_client.v1.model.logs_attribute_remapper_type import LogsAttributeRemapperType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayMapNoPreserve",
    processors=[
        LogsArrayMapProcessor(
            type=LogsArrayMapProcessorType.ARRAY_MAP_PROCESSOR,
            is_enabled=True,
            name="map and remove source",
            source="items",
            target="out",
            preserve_source=False,
            processors=[
                LogsAttributeRemapper(
                    type=LogsAttributeRemapperType.ATTRIBUTE_REMAPPER,
                    sources=[
                        "$sourceElem.id",
                    ],
                    target="$targetElem.uid",
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
