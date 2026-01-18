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
    from datadog_api_client.v2.model.google_chat_create_organization_handle_request_data import (
        GoogleChatCreateOrganizationHandleRequestData,
    )
    from datadog_api_client.v2.model.google_chat_organization_handle_type import GoogleChatOrganizationHandleType


class GoogleChatCreateOrganizationHandleRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_create_organization_handle_request_data import (
            GoogleChatCreateOrganizationHandleRequestData,
        )
        from datadog_api_client.v2.model.google_chat_organization_handle_type import GoogleChatOrganizationHandleType

        return {
            "data": (GoogleChatCreateOrganizationHandleRequestData,),
            "type": (GoogleChatOrganizationHandleType,),
        }

    attribute_map = {
        "data": "data",
        "type": "type",
    }

    def __init__(
        self_, data: GoogleChatCreateOrganizationHandleRequestData, type: GoogleChatOrganizationHandleType, **kwargs
    ):
        """
        Create organization handle request.

        :param data: Organization handle data for a create request.
        :type data: GoogleChatCreateOrganizationHandleRequestData

        :param type: Organization handle resource type.
        :type type: GoogleChatOrganizationHandleType
        """
        super().__init__(kwargs)

        self_.data = data
        self_.type = type
