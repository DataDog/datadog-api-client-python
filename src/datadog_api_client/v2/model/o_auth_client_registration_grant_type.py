# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OAuthClientRegistrationGrantType(ModelSimple):
    """
    OAuth 2.0 grant type that a registered client may use.

    :param value: Must be one of ["authorization_code", "refresh_token"].
    :type value: str
    """

    allowed_values = {
        "authorization_code",
        "refresh_token",
    }
    AUTHORIZATION_CODE: ClassVar["OAuthClientRegistrationGrantType"]
    REFRESH_TOKEN: ClassVar["OAuthClientRegistrationGrantType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OAuthClientRegistrationGrantType.AUTHORIZATION_CODE = OAuthClientRegistrationGrantType("authorization_code")
OAuthClientRegistrationGrantType.REFRESH_TOKEN = OAuthClientRegistrationGrantType("refresh_token")
