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


class LLMObsFrontendInteractionResponseItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_frontend_content import LLMObsFrontendContent
        from datadog_api_client.v2.model.llm_obs_frontend_interaction_type import LLMObsFrontendInteractionType

        return {
            "already_existed": (bool,),
            "content_id": (str,),
            "frontend": (LLMObsFrontendContent,),
            "id": (str,),
            "type": (LLMObsFrontendInteractionType,),
        }

    attribute_map = {
        "already_existed": "already_existed",
        "content_id": "content_id",
        "frontend": "frontend",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        already_existed: bool,
        content_id: str,
        frontend: LLMObsFrontendContent,
        id: str,
        type: LLMObsFrontendInteractionType,
        **kwargs,
    ):
        """
        A frontend interaction result.

        :param already_existed: Whether this interaction already existed in the queue.
        :type already_existed: bool

        :param content_id: Server-generated deterministic identifier derived from the content.
        :type content_id: str

        :param frontend: Web content that makes up a ``frontend`` interaction.
        :type frontend: LLMObsFrontendContent

        :param id: Unique identifier of the interaction.
        :type id: str

        :param type: Type discriminator for a ``frontend`` interaction.
        :type type: LLMObsFrontendInteractionType
        """
        super().__init__(kwargs)

        self_.already_existed = already_existed
        self_.content_id = content_id
        self_.frontend = frontend
        self_.id = id
        self_.type = type
