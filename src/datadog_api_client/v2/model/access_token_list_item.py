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
    from datadog_api_client.v2.model.personal_access_token_attributes import PersonalAccessTokenAttributes
    from datadog_api_client.v2.model.access_token_list_item_relationships import AccessTokenListItemRelationships
    from datadog_api_client.v2.model.access_tokens_type import AccessTokensType


class AccessTokenListItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.personal_access_token_attributes import PersonalAccessTokenAttributes
        from datadog_api_client.v2.model.access_token_list_item_relationships import AccessTokenListItemRelationships
        from datadog_api_client.v2.model.access_tokens_type import AccessTokensType

        return {
            "attributes": (PersonalAccessTokenAttributes,),
            "id": (str,),
            "relationships": (AccessTokenListItemRelationships,),
            "type": (AccessTokensType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[PersonalAccessTokenAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[AccessTokenListItemRelationships, UnsetType] = unset,
        type: Union[AccessTokensType, UnsetType] = unset,
        **kwargs,
    ):
        """
        An access token entry returned by the personal access tokens list endpoint. May represent either a personal or a service access token.

        :param attributes: Attributes of an access token.
        :type attributes: PersonalAccessTokenAttributes, optional

        :param id: ID of the access token.
        :type id: str, optional

        :param relationships: Resources related to the access token entry in the mixed list response.
        :type relationships: AccessTokenListItemRelationships, optional

        :param type: Resource type returned by the access tokens list endpoint. Includes both personal and service access tokens.
        :type type: AccessTokensType, optional
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
