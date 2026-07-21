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
    from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage


class LLMObsPromptSDKDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_prompt_chat_message import LLMObsPromptChatMessage

        return {
            "chat_template": ([LLMObsPromptChatMessage],),
            "labels": ([str],),
            "prompt_id": (str,),
            "prompt_version_uuid": (str,),
            "template": (str,),
            "version": (str,),
        }

    attribute_map = {
        "chat_template": "chat_template",
        "labels": "labels",
        "prompt_id": "prompt_id",
        "prompt_version_uuid": "prompt_version_uuid",
        "template": "template",
        "version": "version",
    }

    def __init__(
        self_,
        chat_template: Union[List[LLMObsPromptChatMessage], UnsetType] = unset,
        labels: Union[List[str], UnsetType] = unset,
        prompt_id: Union[str, UnsetType] = unset,
        prompt_version_uuid: Union[str, UnsetType] = unset,
        template: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a flattened prompt version returned for SDK consumption. Exactly one of ``template`` and ``chat_template`` is returned.

        :param chat_template: Chat template for this prompt version, as a list of role and content messages. Omitted for text templates.
        :type chat_template: [LLMObsPromptChatMessage], optional

        :param labels: Labels attached to the selected version. **Deprecated**.
        :type labels: [str], optional

        :param prompt_id: Customer-provided identifier of the prompt.
        :type prompt_id: str, optional

        :param prompt_version_uuid: Unique identifier of this prompt version.
        :type prompt_version_uuid: str, optional

        :param template: Text template for this prompt version. Omitted for chat templates.
        :type template: str, optional

        :param version: Version identifier for this prompt version. This is the sequential version number unless a user-supplied version identifier was set, in which case that identifier is used instead.
        :type version: str, optional
        """
        if chat_template is not unset:
            kwargs["chat_template"] = chat_template
        if labels is not unset:
            kwargs["labels"] = labels
        if prompt_id is not unset:
            kwargs["prompt_id"] = prompt_id
        if prompt_version_uuid is not unset:
            kwargs["prompt_version_uuid"] = prompt_version_uuid
        if template is not unset:
            kwargs["template"] = template
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)
