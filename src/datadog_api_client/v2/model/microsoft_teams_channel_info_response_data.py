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
    from datadog_api_client.v2.model.microsoft_teams_channel_info_response_attributes import (
        MicrosoftTeamsChannelInfoResponseAttributes,
    )
    from datadog_api_client.v2.model.microsoft_teams_channel_info_type import MicrosoftTeamsChannelInfoType


class MicrosoftTeamsChannelInfoResponseData(ModelNormal):
    validations = {
        "id": {
            "max_length": 255,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_teams_channel_info_response_attributes import (
            MicrosoftTeamsChannelInfoResponseAttributes,
        )
        from datadog_api_client.v2.model.microsoft_teams_channel_info_type import MicrosoftTeamsChannelInfoType

        return {
            "attributes": (MicrosoftTeamsChannelInfoResponseAttributes,),
            "id": (str,),
            "type": (MicrosoftTeamsChannelInfoType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[MicrosoftTeamsChannelInfoResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[MicrosoftTeamsChannelInfoType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Channel data from a response.

        :param attributes: Channel attributes.
        :type attributes: MicrosoftTeamsChannelInfoResponseAttributes, optional

        :param id: The ID of the channel.
        :type id: str, optional

        :param type: Channel info resource type.
        :type type: MicrosoftTeamsChannelInfoType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
