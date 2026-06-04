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
    from datadog_api_client.v2.model.llm_obs_delete_annotations_data_attributes_request import (
        LLMObsDeleteAnnotationsDataAttributesRequest,
    )
    from datadog_api_client.v2.model.llm_obs_annotations_type import LLMObsAnnotationsType


class LLMObsDeleteAnnotationsDataRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_delete_annotations_data_attributes_request import (
            LLMObsDeleteAnnotationsDataAttributesRequest,
        )
        from datadog_api_client.v2.model.llm_obs_annotations_type import LLMObsAnnotationsType

        return {
            "attributes": (LLMObsDeleteAnnotationsDataAttributesRequest,),
            "type": (LLMObsAnnotationsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsDeleteAnnotationsDataAttributesRequest, type: LLMObsAnnotationsType, **kwargs
    ):
        """
        Data object for deleting annotations.

        :param attributes: Attributes for deleting annotations.
        :type attributes: LLMObsDeleteAnnotationsDataAttributesRequest

        :param type: Resource type for LLM Observability annotations.
        :type type: LLMObsAnnotationsType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
