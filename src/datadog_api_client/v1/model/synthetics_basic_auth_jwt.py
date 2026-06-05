# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.synthetics_basic_auth_jwt_add_claims import SyntheticsBasicAuthJWTAddClaims
    from datadog_api_client.v1.model.synthetics_basic_auth_jwt_algorithm import SyntheticsBasicAuthJWTAlgorithm
    from datadog_api_client.v1.model.synthetics_basic_auth_jwt_type import SyntheticsBasicAuthJWTType


class SyntheticsBasicAuthJWT(ModelNormal):
    validations = {
        "expires_in": {
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_basic_auth_jwt_add_claims import SyntheticsBasicAuthJWTAddClaims
        from datadog_api_client.v1.model.synthetics_basic_auth_jwt_algorithm import SyntheticsBasicAuthJWTAlgorithm
        from datadog_api_client.v1.model.synthetics_basic_auth_jwt_type import SyntheticsBasicAuthJWTType

        return {
            "add_claims": (SyntheticsBasicAuthJWTAddClaims,),
            "algorithm": (SyntheticsBasicAuthJWTAlgorithm,),
            "expires_in": (int,),
            "header": (str,),
            "payload": (str,),
            "secret": (str,),
            "token_prefix": (str,),
            "type": (SyntheticsBasicAuthJWTType,),
        }

    attribute_map = {
        "add_claims": "addClaims",
        "algorithm": "algorithm",
        "expires_in": "expiresIn",
        "header": "header",
        "payload": "payload",
        "secret": "secret",
        "token_prefix": "tokenPrefix",
        "type": "type",
    }

    def __init__(
        self_,
        algorithm: SyntheticsBasicAuthJWTAlgorithm,
        payload: str,
        secret: str,
        type: SyntheticsBasicAuthJWTType,
        add_claims: Union[SyntheticsBasicAuthJWTAddClaims, UnsetType] = unset,
        expires_in: Union[int, UnsetType] = unset,
        header: Union[str, UnsetType] = unset,
        token_prefix: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object to handle JWT authentication when performing the test.

        :param add_claims: Standard JWT claims to automatically inject.
        :type add_claims: SyntheticsBasicAuthJWTAddClaims, optional

        :param algorithm: Algorithm to use for the JWT authentication.
        :type algorithm: SyntheticsBasicAuthJWTAlgorithm

        :param expires_in: Token time-to-live in seconds.
        :type expires_in: int, optional

        :param header: Custom JWT header as a JSON string.
        :type header: str, optional

        :param payload: JWT claims as a JSON string.
        :type payload: str

        :param secret: Signing key for the JWT authentication. Use the shared secret for ``HS256``
            or the private key (PEM format) for ``RS256`` and ``ES256``.
        :type secret: str

        :param token_prefix: Prefix added before the token in the ``Authorization`` header. Defaults to ``Bearer``.
        :type token_prefix: str, optional

        :param type: The type of authentication to use when performing the test.
        :type type: SyntheticsBasicAuthJWTType
        """
        if add_claims is not unset:
            kwargs["add_claims"] = add_claims
        if expires_in is not unset:
            kwargs["expires_in"] = expires_in
        if header is not unset:
            kwargs["header"] = header
        if token_prefix is not unset:
            kwargs["token_prefix"] = token_prefix
        super().__init__(kwargs)

        self_.algorithm = algorithm
        self_.payload = payload
        self_.secret = secret
        self_.type = type
