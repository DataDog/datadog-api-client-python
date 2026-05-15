"""
Add a display_block interaction returns "Created" response
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
from datadog_api_client.v2.model.llm_obs_content_block import LLMObsContentBlock
from datadog_api_client.v2.model.llm_obs_content_block_type import LLMObsContentBlockType
from datadog_api_client.v2.model.llm_obs_display_block_interaction_item import LLMObsDisplayBlockInteractionItem
from datadog_api_client.v2.model.llm_obs_display_block_interaction_type import LLMObsDisplayBlockInteractionType

body = LLMObsAnnotationQueueInteractionsRequest(
    data=LLMObsAnnotationQueueInteractionsDataRequest(
        attributes=LLMObsAnnotationQueueInteractionsDataAttributesRequest(
            interactions=[
                LLMObsDisplayBlockInteractionItem(
                    type=LLMObsDisplayBlockInteractionType.DISPLAY_BLOCK,
                    display_block=[
                        LLMObsContentBlock(
                            type=LLMObsContentBlockType.MARKDOWN,
                            content="## Triage Instructions",
                        ),
                    ],
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
