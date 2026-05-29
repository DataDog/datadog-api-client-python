# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AccessTokensType(ModelSimple):
    """
    Resource type returned by the access tokens list endpoint. Includes both personal and service access tokens.

    :param value: Must be one of ["personal_access_tokens", "service_access_tokens"].
    :type value: str
    """

    allowed_values = {
        "personal_access_tokens",
        "service_access_tokens",
    }
    PERSONAL_ACCESS_TOKENS: ClassVar["AccessTokensType"]
    SERVICE_ACCESS_TOKENS: ClassVar["AccessTokensType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AccessTokensType.PERSONAL_ACCESS_TOKENS = AccessTokensType("personal_access_tokens")
AccessTokensType.SERVICE_ACCESS_TOKENS = AccessTokensType("service_access_tokens")
