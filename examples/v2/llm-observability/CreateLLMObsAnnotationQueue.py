"""
Create an LLM Observability annotation queue returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_annotation_queue_data_attributes_request import (
    LLMObsAnnotationQueueDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_data_request import LLMObsAnnotationQueueDataRequest
from datadog_api_client.v2.model.llm_obs_annotation_queue_request import LLMObsAnnotationQueueRequest
from datadog_api_client.v2.model.llm_obs_annotation_queue_type import LLMObsAnnotationQueueType

body = LLMObsAnnotationQueueRequest(
    data=LLMObsAnnotationQueueDataRequest(
        attributes=LLMObsAnnotationQueueDataAttributesRequest(
            description="Queue for annotating customer support traces",
            name="My annotation queue",
            project_id="a33671aa-24fd-4dcd-9b33-a8ec7dde7751",
        ),
        type=LLMObsAnnotationQueueType.QUEUES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_annotation_queue"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_annotation_queue(body=body)

    print(response)
