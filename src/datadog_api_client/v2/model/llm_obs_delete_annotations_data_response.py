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
    from datadog_api_client.v2.model.llm_obs_delete_annotations_data_attributes_response import (
        LLMObsDeleteAnnotationsDataAttributesResponse,
    )
    from datadog_api_client.v2.model.llm_obs_annotations_type import LLMObsAnnotationsType


class LLMObsDeleteAnnotationsDataResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_annotations_data_attributes_response import (
            LLMObsDeleteAnnotationsDataAttributesResponse,
        )
        from datadog_api_client.v2.model.llm_obs_annotations_type import LLMObsAnnotationsType

        return {
            "attributes": (LLMObsDeleteAnnotationsDataAttributesResponse,),
            "id": (str,),
            "type": (LLMObsAnnotationsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsDeleteAnnotationsDataAttributesResponse, id: str, type: LLMObsAnnotationsType, **kwargs
    ):
        """
        Data object for the annotation deletion response.

        :param attributes: Attributes of the annotation deletion response.
        :type attributes: LLMObsDeleteAnnotationsDataAttributesResponse

        :param id: The annotation queue ID.
        :type id: str

        :param type: Resource type for LLM Observability annotations.
        :type type: LLMObsAnnotationsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
