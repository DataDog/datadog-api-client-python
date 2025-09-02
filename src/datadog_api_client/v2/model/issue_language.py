# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueLanguage(ModelSimple):
    """
    Programming language associated with the issue.

    :param value: Must be one of ["BRIGHTSCRIPT", "C", "C_PLUS_PLUS", "C_SHARP", "CLOJURE", "DOT_NET", "ELIXIR", "ERLANG", "GO", "GROOVY", "HASKELL", "HCL", "JAVA", "JAVASCRIPT", "JVM", "KOTLIN", "OBJECTIVE_C", "PERL", "PHP", "PYTHON", "RUBY", "RUST", "SCALA", "SWIFT", "TERRAFORM", "TYPESCRIPT", "UNKNOWN"].
    :type value: str
    """

    allowed_values = {
        "BRIGHTSCRIPT",
        "C",
        "C_PLUS_PLUS",
        "C_SHARP",
        "CLOJURE",
        "DOT_NET",
        "ELIXIR",
        "ERLANG",
        "GO",
        "GROOVY",
        "HASKELL",
        "HCL",
        "JAVA",
        "JAVASCRIPT",
        "JVM",
        "KOTLIN",
        "OBJECTIVE_C",
        "PERL",
        "PHP",
        "PYTHON",
        "RUBY",
        "RUST",
        "SCALA",
        "SWIFT",
        "TERRAFORM",
        "TYPESCRIPT",
        "UNKNOWN",
    }
    BRIGHTSCRIPT: ClassVar["IssueLanguage"]
    C: ClassVar["IssueLanguage"]
    C_PLUS_PLUS: ClassVar["IssueLanguage"]
    C_SHARP: ClassVar["IssueLanguage"]
    CLOJURE: ClassVar["IssueLanguage"]
    DOT_NET: ClassVar["IssueLanguage"]
    ELIXIR: ClassVar["IssueLanguage"]
    ERLANG: ClassVar["IssueLanguage"]
    GO: ClassVar["IssueLanguage"]
    GROOVY: ClassVar["IssueLanguage"]
    HASKELL: ClassVar["IssueLanguage"]
    HCL: ClassVar["IssueLanguage"]
    JAVA: ClassVar["IssueLanguage"]
    JAVASCRIPT: ClassVar["IssueLanguage"]
    JVM: ClassVar["IssueLanguage"]
    KOTLIN: ClassVar["IssueLanguage"]
    OBJECTIVE_C: ClassVar["IssueLanguage"]
    PERL: ClassVar["IssueLanguage"]
    PHP: ClassVar["IssueLanguage"]
    PYTHON: ClassVar["IssueLanguage"]
    RUBY: ClassVar["IssueLanguage"]
    RUST: ClassVar["IssueLanguage"]
    SCALA: ClassVar["IssueLanguage"]
    SWIFT: ClassVar["IssueLanguage"]
    TERRAFORM: ClassVar["IssueLanguage"]
    TYPESCRIPT: ClassVar["IssueLanguage"]
    UNKNOWN: ClassVar["IssueLanguage"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueLanguage.BRIGHTSCRIPT = IssueLanguage("BRIGHTSCRIPT")
IssueLanguage.C = IssueLanguage("C")
IssueLanguage.C_PLUS_PLUS = IssueLanguage("C_PLUS_PLUS")
IssueLanguage.C_SHARP = IssueLanguage("C_SHARP")
IssueLanguage.CLOJURE = IssueLanguage("CLOJURE")
IssueLanguage.DOT_NET = IssueLanguage("DOT_NET")
IssueLanguage.ELIXIR = IssueLanguage("ELIXIR")
IssueLanguage.ERLANG = IssueLanguage("ERLANG")
IssueLanguage.GO = IssueLanguage("GO")
IssueLanguage.GROOVY = IssueLanguage("GROOVY")
IssueLanguage.HASKELL = IssueLanguage("HASKELL")
IssueLanguage.HCL = IssueLanguage("HCL")
IssueLanguage.JAVA = IssueLanguage("JAVA")
IssueLanguage.JAVASCRIPT = IssueLanguage("JAVASCRIPT")
IssueLanguage.JVM = IssueLanguage("JVM")
IssueLanguage.KOTLIN = IssueLanguage("KOTLIN")
IssueLanguage.OBJECTIVE_C = IssueLanguage("OBJECTIVE_C")
IssueLanguage.PERL = IssueLanguage("PERL")
IssueLanguage.PHP = IssueLanguage("PHP")
IssueLanguage.PYTHON = IssueLanguage("PYTHON")
IssueLanguage.RUBY = IssueLanguage("RUBY")
IssueLanguage.RUST = IssueLanguage("RUST")
IssueLanguage.SCALA = IssueLanguage("SCALA")
IssueLanguage.SWIFT = IssueLanguage("SWIFT")
IssueLanguage.TERRAFORM = IssueLanguage("TERRAFORM")
IssueLanguage.TYPESCRIPT = IssueLanguage("TYPESCRIPT")
IssueLanguage.UNKNOWN = IssueLanguage("UNKNOWN")
