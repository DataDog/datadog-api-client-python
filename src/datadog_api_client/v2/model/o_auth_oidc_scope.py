# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OAuthOidcScope(ModelSimple):
    """
    OIDC scope a client may be restricted to.

    :param value: Must be one of ["openid", "profile", "email", "offline_access"].
    :type value: str
    """

    allowed_values = {
        "openid",
        "profile",
        "email",
        "offline_access",
    }
    OPENID: ClassVar["OAuthOidcScope"]
    PROFILE: ClassVar["OAuthOidcScope"]
    EMAIL: ClassVar["OAuthOidcScope"]
    OFFLINE_ACCESS: ClassVar["OAuthOidcScope"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OAuthOidcScope.OPENID = OAuthOidcScope("openid")
OAuthOidcScope.PROFILE = OAuthOidcScope("profile")
OAuthOidcScope.EMAIL = OAuthOidcScope("email")
OAuthOidcScope.OFFLINE_ACCESS = OAuthOidcScope("offline_access")
