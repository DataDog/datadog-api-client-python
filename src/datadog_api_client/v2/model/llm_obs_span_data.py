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
    from datadog_api_client.v2.model.llm_obs_span_attributes import LLMObsSpanAttributes
    from datadog_api_client.v2.model.llm_obs_span_type import LLMObsSpanType


class LLMObsSpanData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_span_attributes import LLMObsSpanAttributes
        from datadog_api_client.v2.model.llm_obs_span_type import LLMObsSpanType

        return {
            "attributes": (LLMObsSpanAttributes,),
            "id": (str,),
            "type": (LLMObsSpanType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsSpanAttributes, id: str, type: LLMObsSpanType, **kwargs):
        """
        A single LLM Observability span.

        :param attributes: Attributes of an LLM Observability span.
        :type attributes: LLMObsSpanAttributes

        :param id: Unique identifier of the span.
        :type id: str

        :param type: Resource type for an LLM Observability span.
        :type type: LLMObsSpanType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
