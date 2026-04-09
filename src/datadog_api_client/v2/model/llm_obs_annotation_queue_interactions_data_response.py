# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_data_attributes_response import (
        LLMObsAnnotationQueueInteractionsDataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_type import (
        LLMObsAnnotationQueueInteractionsType,
    )


class LLMObsAnnotationQueueInteractionsDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_data_attributes_response import (
            LLMObsAnnotationQueueInteractionsDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_annotation_queue_interactions_type import (
            LLMObsAnnotationQueueInteractionsType,
        )

        return {
            "attributes": (LLMObsAnnotationQueueInteractionsDataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsAnnotationQueueInteractionsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsAnnotationQueueInteractionsDataAttributesResponse,
        id: str,
        type: LLMObsAnnotationQueueInteractionsType,
        **kwargs,
    ):
        """
        Data object for the interaction addition response.

        :param attributes: Attributes of the interaction addition response.
        :type attributes: LLMObsAnnotationQueueInteractionsDataAttributesResponse

        :param id: The queue ID the interactions were added to.
        :type id: str

        :param type: Resource type for annotation queue interactions.
        :type type: LLMObsAnnotationQueueInteractionsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
