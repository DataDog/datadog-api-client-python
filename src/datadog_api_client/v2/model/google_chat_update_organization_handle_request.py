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
    from datadog_api_client.v2.model.google_chat_update_organization_handle_request_data import (
        GoogleChatUpdateOrganizationHandleRequestData,
    )
    from datadog_api_client.v2.model.google_chat_organization_handle_type import GoogleChatOrganizationHandleType


class GoogleChatUpdateOrganizationHandleRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_update_organization_handle_request_data import (
            GoogleChatUpdateOrganizationHandleRequestData,
        )
        from datadog_api_client.v2.model.google_chat_organization_handle_type import GoogleChatOrganizationHandleType

        return {
            "data": (GoogleChatUpdateOrganizationHandleRequestData,),
            "type": (GoogleChatOrganizationHandleType,),
        }

    attribute_map = {
        "data": "data",
        "type": "type",
    }

    def __init__(
        self_, data: GoogleChatUpdateOrganizationHandleRequestData, type: GoogleChatOrganizationHandleType, **kwargs
    ):
        """
        Update organization handle request.

        :param data: Organization handle data for an update request.
        :type data: GoogleChatUpdateOrganizationHandleRequestData

        :param type: Organization handle resource type.
        :type type: GoogleChatOrganizationHandleType
        """
        super().__init__(kwargs)

        self_.data = data
        self_.type = type
