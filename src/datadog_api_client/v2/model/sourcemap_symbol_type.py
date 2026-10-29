# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SourcemapSymbolType(ModelSimple):
    """
    The WASM symbol representation.

    :param value: Must be one of ["dwarf", "sourcemap"].
    :type value: str
    """

    allowed_values = {
        "dwarf",
        "sourcemap",
    }
    DWARF: ClassVar["SourcemapSymbolType"]
    SOURCEMAP: ClassVar["SourcemapSymbolType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SourcemapSymbolType.DWARF = SourcemapSymbolType("dwarf")
SourcemapSymbolType.SOURCEMAP = SourcemapSymbolType("sourcemap")
