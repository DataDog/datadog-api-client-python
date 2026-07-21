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
    from datadog_api_client.v2.model.llm_obs_create_prompt_version_data_attributes import (
        LLMObsCreatePromptVersionDataAttributes,
    )
    from datadog_api_client.v2.model.llm_obs_prompt_version_type import LLMObsPromptVersionType


class LLMObsCreatePromptVersionData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_create_prompt_version_data_attributes import (
            LLMObsCreatePromptVersionDataAttributes,
        )
        from datadog_api_client.v2.model.llm_obs_prompt_version_type import LLMObsPromptVersionType

        return {
            "attributes": (LLMObsCreatePromptVersionDataAttributes,),
            "type": (LLMObsPromptVersionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsCreatePromptVersionDataAttributes, type: LLMObsPromptVersionType, **kwargs):
        """
        Data object for creating an LLM Observability prompt version.

        :param attributes: Attributes for creating a new version of an LLM Observability prompt. ``template`` is required; all other attributes are optional.
        :type attributes: LLMObsCreatePromptVersionDataAttributes

        :param type: Resource type of an LLM Observability prompt version.
        :type type: LLMObsPromptVersionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
