# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.full_personal_access_token_attributes import FullPersonalAccessTokenAttributes
    from datadog_api_client.v2.model.personal_access_token_relationships import PersonalAccessTokenRelationships
    from datadog_api_client.v2.model.personal_access_token_type import PersonalAccessTokenType


class FullPersonalAccessToken(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.full_personal_access_token_attributes import FullPersonalAccessTokenAttributes
        from datadog_api_client.v2.model.personal_access_token_relationships import PersonalAccessTokenRelationships
        from datadog_api_client.v2.model.personal_access_token_type import PersonalAccessTokenType

        return {
            "attributes": (FullPersonalAccessTokenAttributes,),
            "id": (UUID,),
            "relationships": (PersonalAccessTokenRelationships,),
            "type": (PersonalAccessTokenType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: FullPersonalAccessTokenAttributes,
        id: UUID,
        relationships: PersonalAccessTokenRelationships,
        type: PersonalAccessTokenType,
        **kwargs,
    ):
        """
        Personal access token object with the secret key value. This is only
        returned when creating a new token.

        :param attributes: Attributes of a personal access token including the secret key value.
            This is only returned when creating a new token.
        :type attributes: FullPersonalAccessTokenAttributes

        :param id: UUID of the personal access token.
        :type id: UUID

        :param relationships: Resources related to the personal access token.
        :type relationships: PersonalAccessTokenRelationships

        :param type: Personal access tokens resource type.
        :type type: PersonalAccessTokenType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
