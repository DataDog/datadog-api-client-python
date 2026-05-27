# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.o_auth_oidc_scope import OAuthOidcScope


class UpsertOAuthScopesRestrictionDataAttributes(ModelNormal):
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

    def __init__(
        self_,
        oidc_scopes: Union[List[OAuthOidcScope], UnsetType] = unset,
        permission_scopes: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of an upsert OAuth2 scopes restriction request.

        :param oidc_scopes: OIDC scopes the client is allowed to request.
        :type oidc_scopes: [OAuthOidcScope], optional

        :param permission_scopes: Datadog permission scopes the client is allowed to request.
            Each value must be a valid permission name.
        :type permission_scopes: [str], optional
        """
        if oidc_scopes is not unset:
            kwargs["oidc_scopes"] = oidc_scopes
        if permission_scopes is not unset:
            kwargs["permission_scopes"] = permission_scopes
        super().__init__(kwargs)
