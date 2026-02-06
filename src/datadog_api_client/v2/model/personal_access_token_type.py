# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PersonalAccessTokenType(ModelSimple):
    """
    Personal access tokens resource type.

    :param value: If omitted defaults to "personal_access_tokens". Must be one of ["personal_access_tokens"].
    :type value: str
    """

    allowed_values = {
        "personal_access_tokens",
    }
    PERSONAL_ACCESS_TOKENS: ClassVar["PersonalAccessTokenType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PersonalAccessTokenType.PERSONAL_ACCESS_TOKENS = PersonalAccessTokenType("personal_access_tokens")
