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
    from datadog_api_client.v2.model.chat_message import ChatMessage
    from datadog_api_client.v2.model.user_context import UserContext


class WorkflowScaffoldAgenticStreamRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.chat_message import ChatMessage
        from datadog_api_client.v2.model.user_context import UserContext

        return {
            "chat_history": ([ChatMessage],),
            "existing_workflow": (dict,),
            "previous_action": (str,),
            "user_context": (UserContext,),
            "user_prompt": (str,),
        }

    attribute_map = {
        "chat_history": "chatHistory",
        "existing_workflow": "existingWorkflow",
        "previous_action": "previousAction",
        "user_context": "userContext",
        "user_prompt": "userPrompt",
    }

    def __init__(
        self_,
        user_prompt: str,
        chat_history: Union[List[ChatMessage], UnsetType] = unset,
        existing_workflow: Union[dict, UnsetType] = unset,
        previous_action: Union[str, UnsetType] = unset,
        user_context: Union[UserContext, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param chat_history: Previous chat messages for iterative workflow generation.
        :type chat_history: [ChatMessage], optional

        :param existing_workflow: The existing workflow specification to modify.
        :type existing_workflow: dict, optional

        :param previous_action: The previous action taken in the workflow generation.
        :type previous_action: str, optional

        :param user_context:
        :type user_context: UserContext, optional

        :param user_prompt: The user's prompt for generating or modifying the workflow.
        :type user_prompt: str
        """
        if chat_history is not unset:
            kwargs["chat_history"] = chat_history
        if existing_workflow is not unset:
            kwargs["existing_workflow"] = existing_workflow
        if previous_action is not unset:
            kwargs["previous_action"] = previous_action
        if user_context is not unset:
            kwargs["user_context"] = user_context
        super().__init__(kwargs)

        self_.user_prompt = user_prompt
