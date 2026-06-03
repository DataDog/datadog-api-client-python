# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SourcemapMapKind(ModelSimple):
    """
    The type of source map.

    :param value: Must be one of ["js", "jvm", "ios", "react", "flutter", "elf", "ndk", "il2cpp"].
    :type value: str
    """

    allowed_values = {
        "js",
        "jvm",
        "ios",
        "react",
        "flutter",
        "elf",
        "ndk",
        "il2cpp",
    }
    JS: ClassVar["SourcemapMapKind"]
    JVM: ClassVar["SourcemapMapKind"]
    IOS: ClassVar["SourcemapMapKind"]
    REACT: ClassVar["SourcemapMapKind"]
    FLUTTER: ClassVar["SourcemapMapKind"]
    ELF: ClassVar["SourcemapMapKind"]
    NDK: ClassVar["SourcemapMapKind"]
    IL2CPP: ClassVar["SourcemapMapKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SourcemapMapKind.JS = SourcemapMapKind("js")
SourcemapMapKind.JVM = SourcemapMapKind("jvm")
SourcemapMapKind.IOS = SourcemapMapKind("ios")
SourcemapMapKind.REACT = SourcemapMapKind("react")
SourcemapMapKind.FLUTTER = SourcemapMapKind("flutter")
SourcemapMapKind.ELF = SourcemapMapKind("elf")
SourcemapMapKind.NDK = SourcemapMapKind("ndk")
SourcemapMapKind.IL2CPP = SourcemapMapKind("il2cpp")
