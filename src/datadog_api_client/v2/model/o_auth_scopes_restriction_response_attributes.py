# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.o_auth_scopes_restriction import OAuthScopesRestriction


class OAuthScopesRestrictionResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.o_auth_scopes_restriction import OAuthScopesRestriction

        return {
            "required_permission_scopes": ([str], none_type),
            "scopes_restriction": (OAuthScopesRestriction,),
        }

    attribute_map = {
        "required_permission_scopes": "required_permission_scopes",
        "scopes_restriction": "scopes_restriction",
    }

    def __init__(
        self_,
        required_permission_scopes: Union[List[str], none_type],
        scopes_restriction: Union[OAuthScopesRestriction, none_type],
        **kwargs,
    ):
        """
        Attributes of an OAuth2 client scopes restriction.

        :param required_permission_scopes: Permission scopes automatically required for this client (for example, mobile-app permission scopes).
            Returns ``null`` when no scopes are required.
        :type required_permission_scopes: [str], none_type

        :param scopes_restriction: Allowlist of OIDC and permission scopes enforced for the OAuth2 client.
        :type scopes_restriction: OAuthScopesRestriction, none_type
        """
        super().__init__(kwargs)

        self_.required_permission_scopes = required_permission_scopes
        self_.scopes_restriction = scopes_restriction
