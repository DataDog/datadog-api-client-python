# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.o_auth_client_registration_grant_type import OAuthClientRegistrationGrantType
    from datadog_api_client.v2.model.o_auth_client_registration_response_type import OAuthClientRegistrationResponseType


class OAuthClientRegistrationResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.o_auth_client_registration_grant_type import OAuthClientRegistrationGrantType
        from datadog_api_client.v2.model.o_auth_client_registration_response_type import (
            OAuthClientRegistrationResponseType,
        )

        return {
            "client_id": (UUID,),
            "client_name": (str,),
            "grant_types": ([OAuthClientRegistrationGrantType],),
            "redirect_uris": ([str],),
            "response_types": ([OAuthClientRegistrationResponseType],),
            "token_endpoint_auth_method": (str,),
        }

    attribute_map = {
        "client_id": "client_id",
        "client_name": "client_name",
        "grant_types": "grant_types",
        "redirect_uris": "redirect_uris",
        "response_types": "response_types",
        "token_endpoint_auth_method": "token_endpoint_auth_method",
    }

    def __init__(
        self_,
        client_id: UUID,
        client_name: str,
        grant_types: List[OAuthClientRegistrationGrantType],
        redirect_uris: List[str],
        response_types: List[OAuthClientRegistrationResponseType],
        token_endpoint_auth_method: str,
        **kwargs,
    ):
        """
        Response payload for a successful OAuth2 dynamic client registration as defined by RFC 7591.

        :param client_id: Unique identifier assigned to the registered client.
        :type client_id: UUID

        :param client_name: Human-readable name of the client.
        :type client_name: str

        :param grant_types: OAuth 2.0 grant types registered for the client.
        :type grant_types: [OAuthClientRegistrationGrantType]

        :param redirect_uris: Redirection URIs registered for the client.
        :type redirect_uris: [str]

        :param response_types: OAuth 2.0 response types registered for the client.
        :type response_types: [OAuthClientRegistrationResponseType]

        :param token_endpoint_auth_method: Authentication method registered for the token endpoint. Always ``none``.
        :type token_endpoint_auth_method: str
        """
        super().__init__(kwargs)

        self_.client_id = client_id
        self_.client_name = client_name
        self_.grant_types = grant_types
        self_.redirect_uris = redirect_uris
        self_.response_types = response_types
        self_.token_endpoint_auth_method = token_endpoint_auth_method
