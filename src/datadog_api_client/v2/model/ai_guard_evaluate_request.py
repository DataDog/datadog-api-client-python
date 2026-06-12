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
    from datadog_api_client.v2.model.ai_guard_message import AIGuardMessage
    from datadog_api_client.v2.model.ai_guard_meta import AIGuardMeta


class AIGuardEvaluateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_message import AIGuardMessage
        from datadog_api_client.v2.model.ai_guard_meta import AIGuardMeta

        return {
            "messages": ([AIGuardMessage],),
            "meta": (AIGuardMeta,),
        }

    attribute_map = {
        "messages": "messages",
        "meta": "meta",
    }

    def __init__(self_, messages: List[AIGuardMessage], meta: Union[AIGuardMeta, UnsetType] = unset, **kwargs):
        """
        The evaluation request payload containing conversation messages and optional metadata.

        :param messages: The list of conversation messages to evaluate. Must contain at least one message.
        :type messages: [AIGuardMessage]

        :param meta: Optional metadata providing context about the originating service and request.
        :type meta: AIGuardMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.messages = messages
