# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel
    from datadog_api_client.v2.model.llm_obs_prompt_template import LLMObsPromptTemplate
    from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage


class LLMObsCreatePromptVersionDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel
        from datadog_api_client.v2.model.llm_obs_prompt_template import LLMObsPromptTemplate

        return {
            "description": (str,),
            "env_ids": ([str],),
            "labels": ([LLMObsPromptVersionLabel],),
            "template": (LLMObsPromptTemplate,),
            "user_version": (str,),
        }

    attribute_map = {
        "description": "description",
        "env_ids": "env_ids",
        "labels": "labels",
        "template": "template",
        "user_version": "user_version",
    }

    def __init__(
        self_,
        template: Union[LLMObsPromptTemplate, str, List[LLMObsPromptChatMessage]],
        description: Union[str, UnsetType] = unset,
        env_ids: Union[List[str], UnsetType] = unset,
        labels: Union[List[LLMObsPromptVersionLabel], UnsetType] = unset,
        user_version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a new version of an LLM Observability prompt. ``template`` is required; all other attributes are optional.

        :param description: Optional description of this version.
        :type description: str, optional

        :param env_ids: Optional feature-flag environment UUIDs the service attempts to enable and configure to use this version as their default after creation.
        :type env_ids: [str], optional

        :param labels: Optional labels to attach to this version. Do not use this attribute for new integrations. **Deprecated**.
        :type labels: [LLMObsPromptVersionLabel], optional

        :param template: A text template or a list of chat messages.
        :type template: LLMObsPromptTemplate

        :param user_version: Optional user-supplied version identifier for this version.
        :type user_version: str, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if env_ids is not unset:
            kwargs["env_ids"] = env_ids
        if labels is not unset:
            kwargs["labels"] = labels
        if user_version is not unset:
            kwargs["user_version"] = user_version
        super().__init__(kwargs)

        self_.template = template
