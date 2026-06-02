# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.webhooks_auth_method_protocol import WebhooksAuthMethodProtocol


class WebhooksOAuth2ClientCredentialsResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.webhooks_auth_method_protocol import WebhooksAuthMethodProtocol

        return {
            "access_token_url": (str,),
            "audience": (str, none_type),
            "client_id": (str,),
            "name": (str,),
            "protocol": (WebhooksAuthMethodProtocol,),
            "scope": (str, none_type),
        }

    attribute_map = {
        "access_token_url": "access_token_url",
        "audience": "audience",
        "client_id": "client_id",
        "name": "name",
        "protocol": "protocol",
        "scope": "scope",
    }

    def __init__(
        self_,
        access_token_url: Union[str, UnsetType] = unset,
        audience: Union[str, none_type, UnsetType] = unset,
        client_id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        protocol: Union[WebhooksAuthMethodProtocol, UnsetType] = unset,
        scope: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        OAuth2 client credentials attributes returned by the API. The ``client_secret`` is never echoed.

        :param access_token_url: URL of the OAuth2 access token endpoint.
        :type access_token_url: str, optional

        :param audience: The intended audience for the OAuth2 access token.
        :type audience: str, none_type, optional

        :param client_id: The OAuth2 client ID issued by the authorization server.
        :type client_id: str, optional

        :param name: Human-readable name for this auth method.
        :type name: str, optional

        :param protocol: Authentication protocol used by the auth method.
        :type protocol: WebhooksAuthMethodProtocol, optional

        :param scope: Space-separated list of OAuth2 scopes to request.
        :type scope: str, none_type, optional
        """
        if access_token_url is not unset:
            kwargs["access_token_url"] = access_token_url
        if audience is not unset:
            kwargs["audience"] = audience
        if client_id is not unset:
            kwargs["client_id"] = client_id
        if name is not unset:
            kwargs["name"] = name
        if protocol is not unset:
            kwargs["protocol"] = protocol
        if scope is not unset:
            kwargs["scope"] = scope
        super().__init__(kwargs)
