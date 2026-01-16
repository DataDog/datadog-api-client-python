# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class Language(ModelSimple):
    """
    Programming language

    :param value: Must be one of ["PYTHON", "JAVASCRIPT", "TYPESCRIPT", "JAVA", "GO", "YAML", "RUBY", "CSHARP", "PHP", "KOTLIN", "SWIFT"].
    :type value: str
    """

    allowed_values = {
        "PYTHON",
        "JAVASCRIPT",
        "TYPESCRIPT",
        "JAVA",
        "GO",
        "YAML",
        "RUBY",
        "CSHARP",
        "PHP",
        "KOTLIN",
        "SWIFT",
    }
    PYTHON: ClassVar["Language"]
    JAVASCRIPT: ClassVar["Language"]
    TYPESCRIPT: ClassVar["Language"]
    JAVA: ClassVar["Language"]
    GO: ClassVar["Language"]
    YAML: ClassVar["Language"]
    RUBY: ClassVar["Language"]
    CSHARP: ClassVar["Language"]
    PHP: ClassVar["Language"]
    KOTLIN: ClassVar["Language"]
    SWIFT: ClassVar["Language"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


Language.PYTHON = Language("PYTHON")
Language.JAVASCRIPT = Language("JAVASCRIPT")
Language.TYPESCRIPT = Language("TYPESCRIPT")
Language.JAVA = Language("JAVA")
Language.GO = Language("GO")
Language.YAML = Language("YAML")
Language.RUBY = Language("RUBY")
Language.CSHARP = Language("CSHARP")
Language.PHP = Language("PHP")
Language.KOTLIN = Language("KOTLIN")
Language.SWIFT = Language("SWIFT")
