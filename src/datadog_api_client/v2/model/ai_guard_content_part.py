# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.ai_guard_image_url import AIGuardImageURL
    from datadog_api_client.v2.model.ai_guard_content_part_type import AIGuardContentPartType


class AIGuardContentPart(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_image_url import AIGuardImageURL
        from datadog_api_client.v2.model.ai_guard_content_part_type import AIGuardContentPartType

        return {
            "image_url": (AIGuardImageURL,),
            "text": (str,),
            "type": (AIGuardContentPartType,),
        }

    attribute_map = {
        "image_url": "image_url",
        "text": "text",
        "type": "type",
    }

    def __init__(
        self_,
        type: AIGuardContentPartType,
        image_url: Union[AIGuardImageURL, UnsetType] = unset,
        text: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        One part of multipart message content, following the OpenAI content part
        format. For user, system, developer, and tool messages, a text part must
        include non-empty ``text`` , and an image part must include ``image_url`` with
        a non-empty ``url``. These content-part checks do not apply to assistant messages.

        :param image_url: An image referenced by URL in a message content part.
        :type image_url: AIGuardImageURL, optional

        :param text: The text content, required and non-empty when ``type`` is ``text`` in a user, system, developer, or tool message.
        :type text: str, optional

        :param type: The type of the content part.
        :type type: AIGuardContentPartType
        """
        if image_url is not unset:
            kwargs["image_url"] = image_url
        if text is not unset:
            kwargs["text"] = text
        super().__init__(kwargs)

        self_.type = type
