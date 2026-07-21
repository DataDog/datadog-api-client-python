# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class LLMObsPromptChatMessage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "content": (str,),
            "role": (str,),
        }

    attribute_map = {
        "content": "content",
        "role": "role",
    }

    def __init__(self_, content: str, role: str, **kwargs):
        """
        A single chat message in a prompt template.

        :param content: Content of the message.
        :type content: str

        :param role: Role of the message (for example ``system`` , ``user`` , or ``assistant`` ).
        :type role: str
        """
        super().__init__(kwargs)

        self_.content = content
        self_.role = role
