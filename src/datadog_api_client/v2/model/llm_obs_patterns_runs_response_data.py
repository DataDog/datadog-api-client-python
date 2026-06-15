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
    from datadog_api_client.v2.model.llm_obs_patterns_runs_response_attributes import (
        LLMObsPatternsRunsResponseAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_patterns_runs_list_type import LLMObsPatternsRunsListType


class LLMObsPatternsRunsResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_runs_response_attributes import (
            LLMObsPatternsRunsResponseAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_patterns_runs_list_type import LLMObsPatternsRunsListType

        return {
            "attributes": (LLMObsPatternsRunsResponseAttributes,),
            "id": (str,),
            "type": (LLMObsPatternsRunsListType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: LLMObsPatternsRunsResponseAttributes, id: str, type: LLMObsPatternsRunsListType, **kwargs
    ):
        """
        Data object of an LLM Observability patterns runs response.

        :param attributes: Attributes of an LLM Observability patterns runs response.
        :type attributes: LLMObsPatternsRunsResponseAttributes

        :param id: Identifier of the configuration the runs belong to.
        :type id: str

        :param type: Resource type of a list of LLM Observability patterns runs.
        :type type: LLMObsPatternsRunsListType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
