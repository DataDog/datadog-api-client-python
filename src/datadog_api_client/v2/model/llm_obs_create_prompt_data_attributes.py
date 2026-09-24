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
    from datadog_api_client.v2.model.llm_obs_prompt_config import LLMObsPromptConfig
    from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel
    from datadog_api_client.v2.model.llm_obs_prompt_template import LLMObsPromptTemplate
    from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage
    from datadog_api_client.v2.model.llm_obs_prompt_authoring_messages_template import (
        LLMObsPromptAuthoringMessagesTemplate,
    )


class LLMObsCreatePromptDataAttributes(ModelNormal):
    validations = {
        "prompt_id": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_config import LLMObsPromptConfig
        from datadog_api_client.v2.model.llm_obs_prompt_version_label import LLMObsPromptVersionLabel
        from datadog_api_client.v2.model.llm_obs_prompt_template import LLMObsPromptTemplate

        return {
            "config": (LLMObsPromptConfig,),
            "description": (str,),
            "env_ids": ([str],),
            "labels": ([LLMObsPromptVersionLabel],),
            "prompt_id": (str,),
            "template": (LLMObsPromptTemplate,),
            "title": (str,),
            "user_version": (str,),
        }

    attribute_map = {
        "config": "config",
        "description": "description",
        "env_ids": "env_ids",
        "labels": "labels",
        "prompt_id": "prompt_id",
        "template": "template",
        "title": "title",
        "user_version": "user_version",
    }

    def __init__(
        self_,
        prompt_id: str,
        template: Union[
            LLMObsPromptTemplate, str, List[LLMObsPromptChatMessage], LLMObsPromptAuthoringMessagesTemplate
        ],
        config: Union[LLMObsPromptConfig, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        env_ids: Union[List[str], UnsetType] = unset,
        labels: Union[List[LLMObsPromptVersionLabel], UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        user_version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an Agent Observability prompt and its first version. ``prompt_id`` and ``template`` are required; all other attributes are optional. If ``config`` is omitted, the first version stores an empty object. Configuration authoring must be enabled for your organization to supply ``config``. Otherwise, supplying it, including an empty object, returns HTTP 403.

        :param config: Versioned prompt configuration is in Preview. To request access, contact `Datadog Support <https://www.datadoghq.com/support/>`_ or your Customer Success Manager. Customer-owned configuration delivered with a prompt version. Datadog stores and returns the object without interpolating it, validating provider-specific keys, or applying it to model calls. Do not include secrets.
        :type config: LLMObsPromptConfig, optional

        :param description: Optional description of the prompt.
        :type description: str, optional

        :param env_ids: Optional feature-flag environment UUIDs the service attempts to enable and configure to use the first version as their default after creation.
        :type env_ids: [str], optional

        :param labels: Optional labels to attach to the first version. Do not use this attribute for new integrations. **Deprecated**.
        :type labels: [LLMObsPromptVersionLabel], optional

        :param prompt_id: Customer-provided identifier for the new prompt.
        :type prompt_id: str

        :param template: A text template, a list of chat messages, or an authored chat object. Text can include an exact prompt version with ``{{>prompt-id version=N}}`` ; other text, including ``{{>...}}`` sequences without a version, remains literal. Use an authored chat object when including prompts as chat messages.
            **Preview** : Prompt composition is available in Preview. To request access, contact `Datadog Support <https://docs.datadoghq.com/help/>`_ or your Customer Success Manager.
            Without access, inline references remain literal text and structured includes are unsupported. Previously compiled prompt versions remain available for execution.
        :type template: LLMObsPromptTemplate

        :param title: Optional title of the prompt.
        :type title: str, optional

        :param user_version: Optional user-supplied version identifier for the first version.
        :type user_version: str, optional
        """
        if config is not unset:
            kwargs["config"] = config
        if description is not unset:
            kwargs["description"] = description
        if env_ids is not unset:
            kwargs["env_ids"] = env_ids
        if labels is not unset:
            kwargs["labels"] = labels
        if title is not unset:
            kwargs["title"] = title
        if user_version is not unset:
            kwargs["user_version"] = user_version
        super().__init__(kwargs)

        self_.prompt_id = prompt_id
        self_.template = template
