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
    from datadog_api_client.v2.model.llm_obs_frontend_content import LLMObsFrontendContent
    from datadog_api_client.v2.model.llm_obs_frontend_interaction_type import LLMObsFrontendInteractionType


class LLMObsFrontendInteractionItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_frontend_content import LLMObsFrontendContent
        from datadog_api_client.v2.model.llm_obs_frontend_interaction_type import LLMObsFrontendInteractionType

        return {
            "frontend": (LLMObsFrontendContent,),
            "type": (LLMObsFrontendInteractionType,),
        }

    attribute_map = {
        "frontend": "frontend",
        "type": "type",
    }

    def __init__(self_, frontend: LLMObsFrontendContent, type: LLMObsFrontendInteractionType, **kwargs):
        """
        An interaction whose rendered content is supplied directly as web
        content. The server generates ``content_id`` deterministically from the
        content.

        :param frontend: Web content that makes up a ``frontend`` interaction.
        :type frontend: LLMObsFrontendContent

        :param type: Type discriminator for a ``frontend`` interaction.
        :type type: LLMObsFrontendInteractionType
        """
        super().__init__(kwargs)

        self_.frontend = frontend
        self_.type = type
