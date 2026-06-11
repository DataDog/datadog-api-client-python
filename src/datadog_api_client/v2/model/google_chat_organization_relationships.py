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
    from datadog_api_client.v2.model.google_chat_organization_relationships_delegated_user import (
        GoogleChatOrganizationRelationshipsDelegatedUser,
    )


class GoogleChatOrganizationRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_organization_relationships_delegated_user import (
            GoogleChatOrganizationRelationshipsDelegatedUser,
        )

        return {
            "delegated_user": (GoogleChatOrganizationRelationshipsDelegatedUser,),
        }

    attribute_map = {
        "delegated_user": "delegated_user",
    }

    def __init__(
        self_, delegated_user: Union[GoogleChatOrganizationRelationshipsDelegatedUser, UnsetType] = unset, **kwargs
    ):
        """
        Google Chat organization relationships.

        :param delegated_user: The delegated user relationship.
        :type delegated_user: GoogleChatOrganizationRelationshipsDelegatedUser, optional
        """
        if delegated_user is not unset:
            kwargs["delegated_user"] = delegated_user
        super().__init__(kwargs)
