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
    from datadog_api_client.v2.model.llm_obs_update_prompt_data_attributes import LLMObsUpdatePromptDataAttributes
    from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType


class LLMObsUpdatePromptData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_update_prompt_data_attributes import LLMObsUpdatePromptDataAttributes
        from datadog_api_client.v2.model.llm_obs_prompt_type import LLMObsPromptType

        return {
            "attributes": (LLMObsUpdatePromptDataAttributes,),
            "type": (LLMObsPromptType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: LLMObsUpdatePromptDataAttributes, type: LLMObsPromptType, **kwargs):
        """
        Data object for updating an LLM Observability prompt.

        :param attributes: Attributes for updating an LLM Observability prompt. At least one of ``title`` or ``description`` must be provided; both attributes are optional individually.
        :type attributes: LLMObsUpdatePromptDataAttributes

        :param type: Resource type of an LLM Observability prompt.
        :type type: LLMObsPromptType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
