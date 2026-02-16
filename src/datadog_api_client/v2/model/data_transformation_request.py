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
    from datadog_api_client.v2.model.chat_history_item import ChatHistoryItem
    from datadog_api_client.v2.model.data_transformation_context import DataTransformationContext
    from datadog_api_client.v2.model.data_transformation_language import DataTransformationLanguage


class DataTransformationRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chat_history_item import ChatHistoryItem
        from datadog_api_client.v2.model.data_transformation_context import DataTransformationContext
        from datadog_api_client.v2.model.data_transformation_language import DataTransformationLanguage

        return {
            "chat_history": ([ChatHistoryItem],),
            "context": (DataTransformationContext,),
            "language": (DataTransformationLanguage,),
            "stream": (bool,),
            "user_prompt": (str,),
        }

    attribute_map = {
        "chat_history": "chatHistory",
        "context": "context",
        "language": "language",
        "stream": "stream",
        "user_prompt": "userPrompt",
    }

    def __init__(
        self_,
        user_prompt: str,
        chat_history: Union[List[ChatHistoryItem], UnsetType] = unset,
        context: Union[DataTransformationContext, UnsetType] = unset,
        language: Union[DataTransformationLanguage, UnsetType] = unset,
        stream: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param chat_history: Previous chat messages for iterative interaction.
        :type chat_history: [ChatHistoryItem], optional

        :param context:
        :type context: DataTransformationContext, optional

        :param language: The programming language for the transformation.
        :type language: DataTransformationLanguage, optional

        :param stream: Whether to stream the response.
        :type stream: bool, optional

        :param user_prompt: The user's prompt describing the desired transformation.
        :type user_prompt: str
        """
        if chat_history is not unset:
            kwargs["chat_history"] = chat_history
        if context is not unset:
            kwargs["context"] = context
        if language is not unset:
            kwargs["language"] = language
        if stream is not unset:
            kwargs["stream"] = stream
        super().__init__(kwargs)

        self_.user_prompt = user_prompt
