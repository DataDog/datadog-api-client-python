# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ResolveVulnerableSymbolsRequestDataType(ModelSimple):
    """


    :param value: If omitted defaults to "resolve-vulnerable-symbols-request". Must be one of ["resolve-vulnerable-symbols-request"].
    :type value: str
    """

    allowed_values = {
        "resolve-vulnerable-symbols-request",
    }
    RESOLVE_VULNERABLE_SYMBOLS_REQUEST: ClassVar["ResolveVulnerableSymbolsRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ResolveVulnerableSymbolsRequestDataType.RESOLVE_VULNERABLE_SYMBOLS_REQUEST = ResolveVulnerableSymbolsRequestDataType(
    "resolve-vulnerable-symbols-request"
)
