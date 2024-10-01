# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.microsoft_teams_api_handle_attributes import MicrosoftTeamsApiHandleAttributes
    from datadog_api_client.v2.model.microsoft_teams_api_handle_type import MicrosoftTeamsApiHandleType


class MicrosoftTeamsUpdateApiHandleRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.microsoft_teams_api_handle_attributes import MicrosoftTeamsApiHandleAttributes
        from datadog_api_client.v2.model.microsoft_teams_api_handle_type import MicrosoftTeamsApiHandleType

        return {
            "attributes": (MicrosoftTeamsApiHandleAttributes,),
            "type": (MicrosoftTeamsApiHandleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: MicrosoftTeamsApiHandleAttributes, type: MicrosoftTeamsApiHandleType, **kwargs):
        """
        Handle data from a response.

        :param attributes: Handle attributes.
        :type attributes: MicrosoftTeamsApiHandleAttributes

        :param type: Specifies the handle resource type.
        :type type: MicrosoftTeamsApiHandleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
