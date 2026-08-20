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


class AIGuardContentPart(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_guard_image_url import AIGuardImageURL

        return {
            "image_url": (AIGuardImageURL,),
            "text": (str,),
            "type": (str,),
        }

    attribute_map = {
        "image_url": "image_url",
        "text": "text",
        "type": "type",
    }

    def __init__(
        self_,
        type: str,
        image_url: Union[AIGuardImageURL, UnsetType] = unset,
        text: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A single part of a multipart message content.

        :param image_url: An image URL reference for multimodal content.
        :type image_url: AIGuardImageURL, optional

        :param text: The text content of this part, required when type is text.
        :type text: str, optional

        :param type: The type of content part, either text or image_url.
        :type type: str
        """
        if image_url is not unset:
            kwargs["image_url"] = image_url
        if text is not unset:
            kwargs["text"] = text
        super().__init__(kwargs)

        self_.type = type
