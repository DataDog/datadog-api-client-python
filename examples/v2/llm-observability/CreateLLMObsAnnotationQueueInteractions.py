"""
Add annotation queue interactions returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_data_attributes_request import (
    LLMObsAnnotationQueueInteractionsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_data_request import (
    LLMObsAnnotationQueueInteractionsDataRequest,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_request import (
    LLMObsAnnotationQueueInteractionsRequest,
)
from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_type import LLMObsAnnotationQueueInteractionsType
from datadog_api_client.v2.model.llm_obs_trace_interaction_item import LLMObsTraceInteractionItem
from datadog_api_client.v2.model.llm_obs_trace_interaction_type import LLMObsTraceInteractionType

body = LLMObsAnnotationQueueInteractionsRequest(
    data=LLMObsAnnotationQueueInteractionsDataRequest(
        attributes=LLMObsAnnotationQueueInteractionsDataAttributesRequest(
            interactions=[
                LLMObsTraceInteractionItem(
                    content_id="trace-abc-123",
                    type=LLMObsTraceInteractionType.TRACE,
                ),
            ],
        ),
        type=LLMObsAnnotationQueueInteractionsType.INTERACTIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_llm_obs_annotation_queue_interactions"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.create_llm_obs_annotation_queue_interactions(queue_id="queue_id", body=body)

    print(response)
