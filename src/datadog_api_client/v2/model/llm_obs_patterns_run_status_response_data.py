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
    from datadog_api_client.v2.model.llm_obs_patterns_run_status_response_attributes import (
        LLMObsPatternsRunStatusResponseAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_patterns_run_status_type import LLMObsPatternsRunStatusType


class LLMObsPatternsRunStatusResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_run_status_response_attributes import (
            LLMObsPatternsRunStatusResponseAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_patterns_run_status_type import LLMObsPatternsRunStatusType

        return {
            "attributes": (LLMObsPatternsRunStatusResponseAttributes,),
            "id": (str,),
            "type": (LLMObsPatternsRunStatusType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: LLMObsPatternsRunStatusResponseAttributes,
        id: str,
        type: LLMObsPatternsRunStatusType,
        **kwargs,
    ):
        """
        Data object of an LLM Observability patterns run status response.

        :param attributes: Attributes of an LLM Observability patterns run status.
        :type attributes: LLMObsPatternsRunStatusResponseAttributes

        :param id: The ID of the patterns run.
        :type id: str

        :param type: Resource type of an LLM Observability patterns run status.
        :type type: LLMObsPatternsRunStatusType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
