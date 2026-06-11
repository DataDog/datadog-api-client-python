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
    from datadog_api_client.v2.model.google_chat_delegated_user_attributes import GoogleChatDelegatedUserAttributes
    from datadog_api_client.v2.model.google_chat_delegated_user_type import GoogleChatDelegatedUserType


class GoogleChatDelegatedUserData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_delegated_user_attributes import GoogleChatDelegatedUserAttributes
        from datadog_api_client.v2.model.google_chat_delegated_user_type import GoogleChatDelegatedUserType

        return {
            "attributes": (GoogleChatDelegatedUserAttributes,),
            "id": (str,),
            "type": (GoogleChatDelegatedUserType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[GoogleChatDelegatedUserAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[GoogleChatDelegatedUserType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Chat delegated user data from a response.

        :param attributes: Google Chat delegated user attributes.
        :type attributes: GoogleChatDelegatedUserAttributes, optional

        :param id: The ID of the delegated user.
        :type id: str, optional

        :param type: Google Chat delegated user resource type.
        :type type: GoogleChatDelegatedUserType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
