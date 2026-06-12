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
    from datadog_api_client.v2.model.google_chat_target_audience_attributes import GoogleChatTargetAudienceAttributes
    from datadog_api_client.v2.model.google_chat_target_audience_type import GoogleChatTargetAudienceType


class GoogleChatTargetAudienceData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_target_audience_attributes import (
            GoogleChatTargetAudienceAttributes,
        )
        from datadog_api_client.v2.model.google_chat_target_audience_type import GoogleChatTargetAudienceType

        return {
            "attributes": (GoogleChatTargetAudienceAttributes,),
            "id": (str,),
            "type": (GoogleChatTargetAudienceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[GoogleChatTargetAudienceAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[GoogleChatTargetAudienceType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Chat target audience data from a response.

        :param attributes: Google Chat target audience attributes.
        :type attributes: GoogleChatTargetAudienceAttributes, optional

        :param id: The ID of the target audience.
        :type id: str, optional

        :param type: Google Chat target audience resource type.
        :type type: GoogleChatTargetAudienceType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
