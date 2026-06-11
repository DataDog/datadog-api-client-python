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
    from datadog_api_client.v2.model.google_chat_organization_attributes import GoogleChatOrganizationAttributes
    from datadog_api_client.v2.model.google_chat_organization_relationships import GoogleChatOrganizationRelationships
    from datadog_api_client.v2.model.google_chat_organization_type import GoogleChatOrganizationType


class GoogleChatOrganizationData(ModelNormal):
    validations = {
        "id": {
            "max_length": 100,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.google_chat_organization_attributes import GoogleChatOrganizationAttributes
        from datadog_api_client.v2.model.google_chat_organization_relationships import (
            GoogleChatOrganizationRelationships,
        )
        from datadog_api_client.v2.model.google_chat_organization_type import GoogleChatOrganizationType

        return {
            "attributes": (GoogleChatOrganizationAttributes,),
            "id": (str,),
            "relationships": (GoogleChatOrganizationRelationships,),
            "type": (GoogleChatOrganizationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[GoogleChatOrganizationAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[GoogleChatOrganizationRelationships, UnsetType] = unset,
        type: Union[GoogleChatOrganizationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Chat organization data from a response.

        :param attributes: Google Chat organization attributes.
        :type attributes: GoogleChatOrganizationAttributes, optional

        :param id: The ID of the Google Chat organization binding.
        :type id: str, optional

        :param relationships: Google Chat organization relationships.
        :type relationships: GoogleChatOrganizationRelationships, optional

        :param type: Google Chat organization resource type.
        :type type: GoogleChatOrganizationType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
