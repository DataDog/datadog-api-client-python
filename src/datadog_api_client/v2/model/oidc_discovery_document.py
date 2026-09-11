# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class OIDCDiscoveryDocument(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "authorization_endpoint": (str,),
            "id_token_signing_alg_values_supported": ([str],),
            "issuer": (str,),
            "jwks_uri": (str,),
            "response_types_supported": ([str],),
            "subject_types_supported": ([str],),
            "token_endpoint": (str,),
        }

    attribute_map = {
        "authorization_endpoint": "authorization_endpoint",
        "id_token_signing_alg_values_supported": "id_token_signing_alg_values_supported",
        "issuer": "issuer",
        "jwks_uri": "jwks_uri",
        "response_types_supported": "response_types_supported",
        "subject_types_supported": "subject_types_supported",
        "token_endpoint": "token_endpoint",
    }

    def __init__(
        self_,
        authorization_endpoint: str,
        id_token_signing_alg_values_supported: List[str],
        issuer: str,
        jwks_uri: str,
        response_types_supported: List[str],
        subject_types_supported: List[str],
        token_endpoint: str,
        **kwargs,
    ):
        """
        OpenID Connect provider metadata.

        :param authorization_endpoint: URL of the OAuth2 authorization endpoint.
        :type authorization_endpoint: str

        :param id_token_signing_alg_values_supported: Signing algorithms supported for ID tokens.
        :type id_token_signing_alg_values_supported: [str]

        :param issuer: URL identifying the OpenID Connect issuer.
        :type issuer: str

        :param jwks_uri: URL of the JSON Web Key Set used to verify ID token signatures.
        :type jwks_uri: str

        :param response_types_supported: OAuth2 response types supported by the provider.
        :type response_types_supported: [str]

        :param subject_types_supported: Subject identifier types supported by the provider.
        :type subject_types_supported: [str]

        :param token_endpoint: URL of the OAuth2 token endpoint.
        :type token_endpoint: str
        """
        super().__init__(kwargs)

        self_.authorization_endpoint = authorization_endpoint
        self_.id_token_signing_alg_values_supported = id_token_signing_alg_values_supported
        self_.issuer = issuer
        self_.jwks_uri = jwks_uri
        self_.response_types_supported = response_types_supported
        self_.subject_types_supported = subject_types_supported
        self_.token_endpoint = token_endpoint
