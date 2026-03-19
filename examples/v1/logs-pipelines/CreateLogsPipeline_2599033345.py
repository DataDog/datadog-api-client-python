"""
Create a pipeline with nested pipeline processor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline
from datadog_api_client.v1.model.logs_pipeline_processor import LogsPipelineProcessor
from datadog_api_client.v1.model.logs_pipeline_processor_type import LogsPipelineProcessorType

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testPipelineWithNested",
    processors=[
        LogsPipelineProcessor(
            type=LogsPipelineProcessorType.PIPELINE,
            is_enabled=True,
            name="nested_pipeline_with_metadata",
            filter=LogsFilter(
                query="env:production",
            ),
            tags=[
                "env:prod",
                "type:nested",
            ],
            description="This is a nested pipeline for production logs",
        ),
    ],
    tags=[
        "team:test",
    ],
    description="Pipeline containing nested processor with tags and description",
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)
