# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class JVMSourcemapMapKind(ModelSimple):
    """
    The type of source map. Always `jvm` for JVM source maps.

    :param value: If omitted defaults to "jvm". Must be one of ["jvm"].
    :type value: str
    """

    allowed_values = {
        "jvm",
    }
    JVM: ClassVar["JVMSourcemapMapKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


JVMSourcemapMapKind.JVM = JVMSourcemapMapKind("jvm")
