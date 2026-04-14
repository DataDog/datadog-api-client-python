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
    from datadog_api_client.v2.model.personal_access_token_relationships import PersonalAccessTokenRelationships
    from datadog_api_client.v2.model.personal_access_tokens_type import PersonalAccessTokensType


class PersonalAccessToken(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.personal_access_token_attributes import PersonalAccessTokenAttributes
        from datadog_api_client.v2.model.personal_access_token_relationships import PersonalAccessTokenRelationships
        from datadog_api_client.v2.model.personal_access_tokens_type import PersonalAccessTokensType

        return {
            "attributes": (PersonalAccessTokenAttributes,),
            "id": (str,),
            "relationships": (PersonalAccessTokenRelationships,),
            "type": (PersonalAccessTokensType,),
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
        relationships: Union[PersonalAccessTokenRelationships, UnsetType] = unset,
        type: Union[PersonalAccessTokensType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Datadog personal access token.

        :param attributes: Attributes of a personal access token.
        :type attributes: PersonalAccessTokenAttributes, optional

        :param id: ID of the personal access token.
        :type id: str, optional

        :param relationships: Resources related to the personal access token.
        :type relationships: PersonalAccessTokenRelationships, optional

        :param type: Personal access tokens resource type.
        :type type: PersonalAccessTokensType, optional
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
