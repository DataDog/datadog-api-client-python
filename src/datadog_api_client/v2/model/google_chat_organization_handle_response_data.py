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
    from datadog_api_client.v2.model.google_chat_organization_handle_response_attributes import (
        GoogleChatOrganizationHandleResponseAttributes,
    )
    from datadog_api_client.v2.model.google_chat_organization_handle_type import GoogleChatOrganizationHandleType


class GoogleChatOrganizationHandleResponseData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_organization_handle_response_attributes import (
            GoogleChatOrganizationHandleResponseAttributes,
        )
        from datadog_api_client.v2.model.google_chat_organization_handle_type import GoogleChatOrganizationHandleType

        return {
            "attributes": (GoogleChatOrganizationHandleResponseAttributes,),
            "id": (str,),
            "type": (GoogleChatOrganizationHandleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[GoogleChatOrganizationHandleResponseAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[GoogleChatOrganizationHandleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Organization handle data from a response.

        :param attributes: Organization handle attributes.
        :type attributes: GoogleChatOrganizationHandleResponseAttributes, optional

        :param id: The ID of the organization handle.
        :type id: str, optional

        :param type: Organization handle resource type.
        :type type: GoogleChatOrganizationHandleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
