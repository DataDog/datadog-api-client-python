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
    from datadog_api_client.v2.model.o_auth_scopes_restriction_response_attributes import (
        OAuthScopesRestrictionResponseAttributes,
    )
    from datadog_api_client.v2.model.o_auth_scopes_restriction_type import OAuthScopesRestrictionType


class OAuthScopesRestrictionResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.o_auth_scopes_restriction_response_attributes import (
            OAuthScopesRestrictionResponseAttributes,
        )
        from datadog_api_client.v2.model.o_auth_scopes_restriction_type import OAuthScopesRestrictionType

        return {
            "attributes": (OAuthScopesRestrictionResponseAttributes,),
            "id": (UUID,),
            "type": (OAuthScopesRestrictionType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: OAuthScopesRestrictionResponseAttributes,
        id: UUID,
        type: OAuthScopesRestrictionType,
        **kwargs,
    ):
        """
        Data object of an OAuth2 client scopes restriction response.

        :param attributes: Attributes of an OAuth2 client scopes restriction.
        :type attributes: OAuthScopesRestrictionResponseAttributes

        :param id: UUID of the OAuth2 client this restriction applies to.
        :type id: UUID

        :param type: JSON:API resource type for an OAuth2 client scopes restriction.
        :type type: OAuthScopesRestrictionType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
