# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OAuthClientRegistrationResponseType(ModelSimple):
    """
    OAuth 2.0 response type that a registered client may use.

    :param value: If omitted defaults to "code". Must be one of ["code"].
    :type value: str
    """

    allowed_values = {
        "code",
    }
    CODE: ClassVar["OAuthClientRegistrationResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OAuthClientRegistrationResponseType.CODE = OAuthClientRegistrationResponseType("code")
