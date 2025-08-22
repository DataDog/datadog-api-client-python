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

    :param value: Must be one of ["javascript", "jvm", "ruby", "typescript", "java", "kotlin", "scala", "groovy", "clojure", "go", "python", "php", "dot_net", "c_sharp", "c_plus_plus", "objective_c", "swift", "brightscript", "c", "elixir", "erlang", "perl", "haskell", "rust"].
    :type value: str
    """

    allowed_values = {
        "javascript",
        "jvm",
        "ruby",
        "typescript",
        "java",
        "kotlin",
        "scala",
        "groovy",
        "clojure",
        "go",
        "python",
        "php",
        "dot_net",
        "c_sharp",
        "c_plus_plus",
        "objective_c",
        "swift",
        "brightscript",
        "c",
        "elixir",
        "erlang",
        "perl",
        "haskell",
        "rust",
    }
    JAVASCRIPT: ClassVar["IssueLanguage"]
    JVM: ClassVar["IssueLanguage"]
    RUBY: ClassVar["IssueLanguage"]
    TYPESCRIPT: ClassVar["IssueLanguage"]
    JAVA: ClassVar["IssueLanguage"]
    KOTLIN: ClassVar["IssueLanguage"]
    SCALA: ClassVar["IssueLanguage"]
    GROOVY: ClassVar["IssueLanguage"]
    CLOJURE: ClassVar["IssueLanguage"]
    GO: ClassVar["IssueLanguage"]
    PYTHON: ClassVar["IssueLanguage"]
    PHP: ClassVar["IssueLanguage"]
    DOT_NET: ClassVar["IssueLanguage"]
    C_SHARP: ClassVar["IssueLanguage"]
    C_PLUS_PLUS: ClassVar["IssueLanguage"]
    OBJECTIVE_C: ClassVar["IssueLanguage"]
    SWIFT: ClassVar["IssueLanguage"]
    BRIGHTSCRIPT: ClassVar["IssueLanguage"]
    C: ClassVar["IssueLanguage"]
    ELIXIR: ClassVar["IssueLanguage"]
    ERLANG: ClassVar["IssueLanguage"]
    PERL: ClassVar["IssueLanguage"]
    HASKELL: ClassVar["IssueLanguage"]
    RUST: ClassVar["IssueLanguage"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueLanguage.JAVASCRIPT = IssueLanguage("javascript")
IssueLanguage.JVM = IssueLanguage("jvm")
IssueLanguage.RUBY = IssueLanguage("ruby")
IssueLanguage.TYPESCRIPT = IssueLanguage("typescript")
IssueLanguage.JAVA = IssueLanguage("java")
IssueLanguage.KOTLIN = IssueLanguage("kotlin")
IssueLanguage.SCALA = IssueLanguage("scala")
IssueLanguage.GROOVY = IssueLanguage("groovy")
IssueLanguage.CLOJURE = IssueLanguage("clojure")
IssueLanguage.GO = IssueLanguage("go")
IssueLanguage.PYTHON = IssueLanguage("python")
IssueLanguage.PHP = IssueLanguage("php")
IssueLanguage.DOT_NET = IssueLanguage("dot_net")
IssueLanguage.C_SHARP = IssueLanguage("c_sharp")
IssueLanguage.C_PLUS_PLUS = IssueLanguage("c_plus_plus")
IssueLanguage.OBJECTIVE_C = IssueLanguage("objective_c")
IssueLanguage.SWIFT = IssueLanguage("swift")
IssueLanguage.BRIGHTSCRIPT = IssueLanguage("brightscript")
IssueLanguage.C = IssueLanguage("c")
IssueLanguage.ELIXIR = IssueLanguage("elixir")
IssueLanguage.ERLANG = IssueLanguage("erlang")
IssueLanguage.PERL = IssueLanguage("perl")
IssueLanguage.HASKELL = IssueLanguage("haskell")
IssueLanguage.RUST = IssueLanguage("rust")
