"""
Create or update annotations returns "OK — annotations created or updated. Per-item errors are listed in `errors`."
response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_annotation_label_value import LLMObsAnnotationLabelValue
from datadog_api_client.v2.model.llm_obs_annotations_data_attributes_request import (
    LLMObsAnnotationsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_annotations_data_request import LLMObsAnnotationsDataRequest
from datadog_api_client.v2.model.llm_obs_annotations_request import LLMObsAnnotationsRequest
from datadog_api_client.v2.model.llm_obs_annotations_type import LLMObsAnnotationsType
from datadog_api_client.v2.model.llm_obs_upsert_annotation_item import LLMObsUpsertAnnotationItem

body = LLMObsAnnotationsRequest(
    data=LLMObsAnnotationsDataRequest(
        attributes=LLMObsAnnotationsDataAttributesRequest(
            annotations=[
                LLMObsUpsertAnnotationItem(
                    interaction_id="00000000-0000-0000-0000-000000000001",
                    label_values=[
                        LLMObsAnnotationLabelValue(
                            label_schema_id="abc-123",
                            value="good",
                        ),
                        LLMObsAnnotationLabelValue(
                            label_schema_id="ef56gh78",
                            value="positive",
                        ),
                    ],
                ),
            ],
        ),
        type=LLMObsAnnotationsType.ANNOTATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["upsert_llm_obs_annotations"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.upsert_llm_obs_annotations(queue_id="queue_id", body=body)

    print(response)
