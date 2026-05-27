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
    from datadog_api_client.v2.model.o_auth_client_registration_grant_type import OAuthClientRegistrationGrantType
    from datadog_api_client.v2.model.o_auth_client_registration_response_type import OAuthClientRegistrationResponseType


class OAuthClientRegistrationRequest(ModelNormal):
    validations = {
        "client_name": {
            "max_length": 1000,
        },
        "client_uri": {
            "max_length": 1000,
        },
        "jwks_uri": {
            "max_length": 1000,
        },
        "logo_uri": {
            "max_length": 1000,
        },
        "policy_uri": {
            "max_length": 1000,
        },
        "scope": {
            "max_length": 1000,
        },
        "token_endpoint_auth_method": {
            "max_length": 20,
        },
        "tos_uri": {
            "max_length": 1000,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.o_auth_client_registration_grant_type import OAuthClientRegistrationGrantType
        from datadog_api_client.v2.model.o_auth_client_registration_response_type import (
            OAuthClientRegistrationResponseType,
        )

        return {
            "client_name": (str,),
            "client_uri": (str,),
            "grant_types": ([OAuthClientRegistrationGrantType],),
            "jwks_uri": (str,),
            "logo_uri": (str,),
            "policy_uri": (str,),
            "redirect_uris": ([str],),
            "response_types": ([OAuthClientRegistrationResponseType],),
            "scope": (str,),
            "token_endpoint_auth_method": (str,),
            "tos_uri": (str,),
        }

    attribute_map = {
        "client_name": "client_name",
        "client_uri": "client_uri",
        "grant_types": "grant_types",
        "jwks_uri": "jwks_uri",
        "logo_uri": "logo_uri",
        "policy_uri": "policy_uri",
        "redirect_uris": "redirect_uris",
        "response_types": "response_types",
        "scope": "scope",
        "token_endpoint_auth_method": "token_endpoint_auth_method",
        "tos_uri": "tos_uri",
    }

    def __init__(
        self_,
        client_name: str,
        redirect_uris: List[str],
        client_uri: Union[str, UnsetType] = unset,
        grant_types: Union[List[OAuthClientRegistrationGrantType], UnsetType] = unset,
        jwks_uri: Union[str, UnsetType] = unset,
        logo_uri: Union[str, UnsetType] = unset,
        policy_uri: Union[str, UnsetType] = unset,
        response_types: Union[List[OAuthClientRegistrationResponseType], UnsetType] = unset,
        scope: Union[str, UnsetType] = unset,
        token_endpoint_auth_method: Union[str, UnsetType] = unset,
        tos_uri: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request payload for OAuth2 dynamic client registration as defined by RFC 7591.

        :param client_name: Human-readable name of the client. Control characters are rejected.
        :type client_name: str

        :param client_uri: URL of the home page of the client.
        :type client_uri: str, optional

        :param grant_types: OAuth 2.0 grant types the client may use.
            Defaults to ``authorization_code`` and ``refresh_token`` when omitted.
        :type grant_types: [OAuthClientRegistrationGrantType], optional

        :param jwks_uri: URL referencing the client's JSON Web Key Set.
        :type jwks_uri: str, optional

        :param logo_uri: URL referencing a logo for the client.
        :type logo_uri: str, optional

        :param policy_uri: URL pointing to the client's privacy policy.
        :type policy_uri: str, optional

        :param redirect_uris: Array of redirection URI strings used by the client in redirect-based flows.
        :type redirect_uris: [str]

        :param response_types: OAuth 2.0 response types the client may use. Only ``code`` is supported.
        :type response_types: [OAuthClientRegistrationResponseType], optional

        :param scope: Space-separated list of scope values the client may request.
        :type scope: str, optional

        :param token_endpoint_auth_method: Requested authentication method for the token endpoint. Only ``none`` is supported.
        :type token_endpoint_auth_method: str, optional

        :param tos_uri: URL pointing to the client's terms of service.
        :type tos_uri: str, optional
        """
        if client_uri is not unset:
            kwargs["client_uri"] = client_uri
        if grant_types is not unset:
            kwargs["grant_types"] = grant_types
        if jwks_uri is not unset:
            kwargs["jwks_uri"] = jwks_uri
        if logo_uri is not unset:
            kwargs["logo_uri"] = logo_uri
        if policy_uri is not unset:
            kwargs["policy_uri"] = policy_uri
        if response_types is not unset:
            kwargs["response_types"] = response_types
        if scope is not unset:
            kwargs["scope"] = scope
        if token_endpoint_auth_method is not unset:
            kwargs["token_endpoint_auth_method"] = token_endpoint_auth_method
        if tos_uri is not unset:
            kwargs["tos_uri"] = tos_uri
        super().__init__(kwargs)

        self_.client_name = client_name
        self_.redirect_uris = redirect_uris
