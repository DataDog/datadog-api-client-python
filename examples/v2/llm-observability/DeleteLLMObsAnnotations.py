"""
Delete annotations returns "OK — annotations deleted. Errors for annotations that could not be deleted are listed in
`errors`." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.llm_observability_api import LLMObservabilityApi
from datadog_api_client.v2.model.llm_obs_annotations_type import LLMObsAnnotationsType
from datadog_api_client.v2.model.llm_obs_delete_annotations_data_attributes_request import (
    LLMObsDeleteAnnotationsDataAttributesRequest,
)
from datadog_api_client.v2.model.llm_obs_delete_annotations_data_request import LLMObsDeleteAnnotationsDataRequest
from datadog_api_client.v2.model.llm_obs_delete_annotations_request import LLMObsDeleteAnnotationsRequest

body = LLMObsDeleteAnnotationsRequest(
    data=LLMObsDeleteAnnotationsDataRequest(
        attributes=LLMObsDeleteAnnotationsDataAttributesRequest(
            annotation_ids=[
                "00000000-0000-0000-0000-000000000000",
                "00000000-0000-0000-0000-000000000001",
            ],
        ),
        type=LLMObsAnnotationsType.ANNOTATIONS,
    ),
)

configuration = Configuration()
configuration.unstable_operations["delete_llm_obs_annotations"] = True
with ApiClient(configuration) as api_client:
    api_instance = LLMObservabilityApi(api_client)
    response = api_instance.delete_llm_obs_annotations(queue_id="queue_id", body=body)

    print(response)
