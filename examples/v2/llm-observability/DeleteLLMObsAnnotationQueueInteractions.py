"""
Delete annotation queue interactions returns "No Content" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_type import LLMObsAnnotationQueueInteractionsType
from datadog_api_client.v2.model.llm_obs_delete_annotation_queue_interactions_data_attributes_request import (
    LLMObsDeleteAnnotationQueueInteractionsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_annotation_queue_interactions_data_request import (
    LLMObsDeleteAnnotationQueueInteractionsDataRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_annotation_queue_interactions_request import (
    LLMObsDeleteAnnotationQueueInteractionsRequest,
)

body = LLMObsDeleteAnnotationQueueInteractionsRequest(
    data=LLMObsDeleteAnnotationQueueInteractionsDataRequest(
        attributes=LLMObsDeleteAnnotationQueueInteractionsDataAttributesRequest(
            interaction_ids=[
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000001",
            ],
        ),
        type=LLMObsAnnotationQueueInteractionsType.INTERACTIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_annotation_queue_interactions"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    api_instance.delete_llm_obs_annotation_queue_interactions(queue_id="queue_id", body=body)
