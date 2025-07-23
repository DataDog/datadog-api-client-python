"""
Create a pipeline with Decoder Processor returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v1.api.logs_pipelines_api import LogsPipelinesApi
from datadog_api_client.v1.model.logs_decoder_processor import LogsDecoderProcessor
from datadog_api_client.v1.model.logs_decoder_processor_binary_to_text_encoding import (
    LogsDecoderProcessorBinaryToTextEncoding,
)
from datadog_api_client.v1.model.logs_decoder_processor_input_representation import (
    LogsDecoderProcessorInputRepresentation,
)
from datadog_api_client.v1.model.logs_decoder_processor_type import LogsDecoderProcessorType
from datadog_api_client.v1.model.logs_filter import LogsFilter
from datadog_api_client.v1.model.logs_pipeline import LogsPipeline

body = LogsPipeline(
    filter=LogsFilter(
        query="source:python",
    ),
    name="testDecoderProcessor",
    processors=[
        LogsDecoderProcessor(
            type=LogsDecoderProcessorType.DECODER_PROCESSOR,
            is_enabled=True,
            name="test_decoder",
            source="encoded.field",
            target="decoded.field",
            binary_to_text_encoding=LogsDecoderProcessorBinaryToTextEncoding.BASE16,
            input_representation=LogsDecoderProcessorInputRepresentation.UTF_8,
        ),
    ],
    tags=[],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsPipelinesApi(api_client)
    response = api_instance.create_logs_pipeline(body=body)

    print(response)
