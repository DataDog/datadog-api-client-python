# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DelegatedTokenType(ModelSimple):
    """
    The resource type for a delegated token.

    :param value: If omitted defaults to "token". Must be one of ["token"].
    :type value: str
    """

    allowed_values = {
        "token",
    }
    TOKEN: ClassVar["DelegatedTokenType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DelegatedTokenType.TOKEN = DelegatedTokenType("token")
