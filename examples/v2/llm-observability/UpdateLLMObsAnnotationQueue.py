"""
Update an LLM Observability annotation queue returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_annotation_queue_type import LLMObsAnnotationQueueType
from datadog_api_client.v2.model.llm_obs_annotation_queue_update_data_attributes_request import (
    LLMObsAnnotationQueueUpdateDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_update_data_request import (
    LLMObsAnnotationQueueUpdateDataRequest,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_update_request import LLMObsAnnotationQueueUpdateRequest

body = LLMObsAnnotationQueueUpdateRequest(
    data=LLMObsAnnotationQueueUpdateDataRequest(
        attributes=LLMObsAnnotationQueueUpdateDataAttributesRequest(
            description="Updated description",
            name="Updated queue name",
        ),
        type=LLMObsAnnotationQueueType.QUEUES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_llm_obs_annotation_queue"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.update_llm_obs_annotation_queue(queue_id="queue_id", body=body)

    print(response)
