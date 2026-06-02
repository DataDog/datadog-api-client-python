# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class WebhooksOAuth2ClientCredentialsUpdateAttributes(ModelNormal):
    validations = {
        "access_token_url": {
            "max_length": 2048,
            "min_length": 1,
        },
        "audience": {
            "max_length": 2048,
            "min_length": 1,
        },
        "client_id": {
            "max_length": 2048,
            "min_length": 1,
        },
        "client_secret": {
            "max_length": 2048,
            "min_length": 1,
        },
        "name": {
            "max_length": 100,
            "min_length": 1,
        },
        "scope": {
            "max_length": 2048,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "access_token_url": (str,),
            "audience": (str, none_type),
            "client_id": (str,),
            "client_secret": (str,),
            "name": (str,),
            "scope": (str, none_type),
        }

    attribute_map = {
        "access_token_url": "access_token_url",
        "audience": "audience",
        "client_id": "client_id",
        "client_secret": "client_secret",
        "name": "name",
        "scope": "scope",
    }

    def __init__(
        self_,
        access_token_url: Union[str, UnsetType] = unset,
        audience: Union[str, none_type, UnsetType] = unset,
        client_id: Union[str, UnsetType] = unset,
        client_secret: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        scope: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        OAuth2 client credentials attributes for an update request.

        :param access_token_url: URL of the OAuth2 access token endpoint.
        :type access_token_url: str, optional

        :param audience: The intended audience for the OAuth2 access token.
        :type audience: str, none_type, optional

        :param client_id: The OAuth2 client ID issued by the authorization server.
        :type client_id: str, optional

        :param client_secret: The OAuth2 client secret issued by the authorization server.
            Write-only; never returned by the API.
        :type client_secret: str, optional

        :param name: Human-readable name for this auth method.
        :type name: str, optional

        :param scope: Space-separated list of OAuth2 scopes to request.
        :type scope: str, none_type, optional
        """
        if access_token_url is not unset:
            kwargs["access_token_url"] = access_token_url
        if audience is not unset:
            kwargs["audience"] = audience
        if client_id is not unset:
            kwargs["client_id"] = client_id
        if client_secret is not unset:
            kwargs["client_secret"] = client_secret
        if name is not unset:
            kwargs["name"] = name
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)
