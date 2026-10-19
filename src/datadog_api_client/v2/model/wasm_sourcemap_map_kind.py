# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class WASMSourcemapMapKind(ModelSimple):
    """
    The type of source map. Always `wasm` for WebAssembly symbol files.

    :param value: If omitted defaults to "wasm". Must be one of ["wasm"].
    :type value: str
    """

    allowed_values = {
        "wasm",
    }
    WASM: ClassVar["WASMSourcemapMapKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


WASMSourcemapMapKind.WASM = WASMSourcemapMapKind("wasm")
