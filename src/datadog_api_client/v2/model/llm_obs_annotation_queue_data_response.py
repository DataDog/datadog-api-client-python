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
    from datadog_api_client.v2.model.llm_obs_annotation_queue_data_attributes_response import (
        LLMObsAnnotationQueueDataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_annotation_queue_type import LLMObsAnnotationQueueType


class LLMObsAnnotationQueueDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_annotation_queue_data_attributes_response import (
            LLMObsAnnotationQueueDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_annotation_queue_type import LLMObsAnnotationQueueType

        return {
            "attributes": (LLMObsAnnotationQueueDataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsAnnotationQueueType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsAnnotationQueueDataAttributesResponse,
        id: str,
        type: LLMObsAnnotationQueueType,
        **kwargs,
    ):
        """
        Data object for an LLM Observability annotation queue.

        :param attributes: Attributes of an LLM Observability annotation queue.
        :type attributes: LLMObsAnnotationQueueDataAttributesResponse

        :param id: Unique identifier of the annotation queue.
        :type id: str

        :param type: Resource type of an LLM Observability annotation queue.
        :type type: LLMObsAnnotationQueueType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
