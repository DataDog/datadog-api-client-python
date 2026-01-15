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
    from datadog_api_client.v2.model.google_chat_create_organization_handle_request_attributes import (
        GoogleChatCreateOrganizationHandleRequestAttributes,
    )


class GoogleChatCreateOrganizationHandleRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_create_organization_handle_request_attributes import (
            GoogleChatCreateOrganizationHandleRequestAttributes,
        )

        return {
            "attributes": (GoogleChatCreateOrganizationHandleRequestAttributes,),
        }

    attribute_map = {
        "attributes": "attributes",
    }

    def __init__(self_, attributes: GoogleChatCreateOrganizationHandleRequestAttributes, **kwargs):
        """
        Organization handle data for a create request.

        :param attributes: Organization handle attributes for a create request.
        :type attributes: GoogleChatCreateOrganizationHandleRequestAttributes
        """
        super().__init__(kwargs)

        self_.attributes = attributes
