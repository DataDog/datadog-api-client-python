# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.o_auth_oidc_scope import OAuthOidcScope


class OAuthScopesRestriction(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.o_auth_oidc_scope import OAuthOidcScope

        return {
            "oidc_scopes": ([OAuthOidcScope],),
            "permission_scopes": ([str],),
        }

    attribute_map = {
        "oidc_scopes": "oidc_scopes",
        "permission_scopes": "permission_scopes",
    }

    def __init__(self_, oidc_scopes: List[OAuthOidcScope], permission_scopes: List[str], **kwargs):
        """
        Allowlist of OIDC and permission scopes enforced for the OAuth2 client.

        :param oidc_scopes: OIDC scopes the client is restricted to.
        :type oidc_scopes: [OAuthOidcScope]

        :param permission_scopes: Datadog permission scopes the client is restricted to.
        :type permission_scopes: [str]
        """
        super().__init__(kwargs)

        self_.oidc_scopes = oidc_scopes
        self_.permission_scopes = permission_scopes
