"""
Create a pipeline with Array Map Processor using category sub-processor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_array_map_category_sub_processor import LogsArrayMapCategorySubProcessor
from datadog_api_client.v1.model.logs_array_map_processor import LogsArrayMapProcessor
from datadog_api_client.v1.model.logs_array_map_processor_type import LogsArrayMapProcessorType
from datadog_api_client.v1.model.logs_category_processor_category import LogsCategoryProcessorCategory
from datadog_api_client.v1.model.logs_category_processor_type import LogsCategoryProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineArrayMapCategory",
    processors=[
        LogsArrayMapProcessor(
            type=LogsArrayMapProcessorType.ARRAY_MAP_PROCESSOR,
            is_enabled=True,
            name="categorize items",
            source="items",
            target="out",
            processors=[
                LogsArrayMapCategorySubProcessor(
                    type=LogsCategoryProcessorType.CATEGORY_PROCESSOR,
                    target="$targetElem.level",
                    categories=[
                        LogsCategoryProcessorCategory(
                            filter=LogsFilter(
                                query="@$sourceElem.status:error",
                            ),
                            name="error",
                        ),
                        LogsCategoryProcessorCategory(
                            filter=LogsFilter(
                                query="*",
                            ),
                            name="info",
                        ),
                    ],
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
