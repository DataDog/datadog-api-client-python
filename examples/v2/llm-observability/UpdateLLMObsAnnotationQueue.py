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
from datadog_api_client.v2.model.llm_obs_annotation_schema import LLMObsAnnotationSchema
from datadog_api_client.v2.model.llm_obs_label_schema import LLMObsLabelSchema
from datadog_api_client.v2.model.llm_obs_label_schema_type import LLMObsLabelSchemaType

body = LLMObsAnnotationQueueUpdateRequest(
    data=LLMObsAnnotationQueueUpdateDataRequest(
        attributes=LLMObsAnnotationQueueUpdateDataAttributesRequest(
            annotation_schema=LLMObsAnnotationSchema(
                label_schemas=[
                    LLMObsLabelSchema(
                        description="Rating of the response quality.",
                        has_assessment=False,
                        has_reasoning=False,
                        id="abc-123",
                        is_assessment=False,
                        is_integer=False,
                        is_required=True,
                        max=5.0,
                        min=0.0,
                        name="quality",
                        type=LLMObsLabelSchemaType.SCORE,
                        values=[
                            "good",
                            "bad",
                            "neutral",
                        ],
                    ),
                ],
            ),
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
