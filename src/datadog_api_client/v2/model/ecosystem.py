# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Ecosystem(ModelSimple):
    """
    The related vulnerability asset ecosystem.

    :param value: Must be one of ["PyPI", "Maven", "NuGet", "Npm", "RubyGems", "Go", "Packagist", "Ddeb", "Rpm", "Apk", "Windows"].
    :type value: str
    """

    allowed_values = {
        "PyPI",
        "Maven",
        "NuGet",
        "Npm",
        "RubyGems",
        "Go",
        "Packagist",
        "Ddeb",
        "Rpm",
        "Apk",
        "Windows",
    }
    PYPI: ClassVar["Ecosystem"]
    MAVEN: ClassVar["Ecosystem"]
    NUGET: ClassVar["Ecosystem"]
    NPM: ClassVar["Ecosystem"]
    RUBYGEMS: ClassVar["Ecosystem"]
    GO: ClassVar["Ecosystem"]
    PACKAGIST: ClassVar["Ecosystem"]
    DDEB: ClassVar["Ecosystem"]
    RPM: ClassVar["Ecosystem"]
    APK: ClassVar["Ecosystem"]
    WINDOWS: ClassVar["Ecosystem"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Ecosystem.PYPI = Ecosystem("PyPI")
Ecosystem.MAVEN = Ecosystem("Maven")
Ecosystem.NUGET = Ecosystem("NuGet")
Ecosystem.NPM = Ecosystem("Npm")
Ecosystem.RUBYGEMS = Ecosystem("RubyGems")
Ecosystem.GO = Ecosystem("Go")
Ecosystem.PACKAGIST = Ecosystem("Packagist")
Ecosystem.DDEB = Ecosystem("Ddeb")
Ecosystem.RPM = Ecosystem("Rpm")
Ecosystem.APK = Ecosystem("Apk")
Ecosystem.WINDOWS = Ecosystem("Windows")
