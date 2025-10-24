# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ResolveVulnerableSymbolsResponseDataType(ModelSimple):
    """


    :param value: If omitted defaults to "resolve-vulnerable-symbols-response". Must be one of ["resolve-vulnerable-symbols-response"].
    :type value: str
    """

    allowed_values = {
        "resolve-vulnerable-symbols-response",
    }
    RESOLVE_VULNERABLE_SYMBOLS_RESPONSE: ClassVar["ResolveVulnerableSymbolsResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ResolveVulnerableSymbolsResponseDataType.RESOLVE_VULNERABLE_SYMBOLS_RESPONSE = ResolveVulnerableSymbolsResponseDataType(
    "resolve-vulnerable-symbols-response"
)
