# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssueStreamPersona(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["all", "browser", "mobile", "backend", "agent"].
    :type value: str
    """

    allowed_values = {
        "all",
        "browser",
        "mobile",
        "backend",
        "agent",
    }
    ALL: ClassVar["IssueStreamPersona"]
    BROWSER: ClassVar["IssueStreamPersona"]
    MOBILE: ClassVar["IssueStreamPersona"]
    BACKEND: ClassVar["IssueStreamPersona"]
    AGENT: ClassVar["IssueStreamPersona"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssueStreamPersona.ALL = IssueStreamPersona("all")
IssueStreamPersona.BROWSER = IssueStreamPersona("browser")
IssueStreamPersona.MOBILE = IssueStreamPersona("mobile")
IssueStreamPersona.BACKEND = IssueStreamPersona("backend")
IssueStreamPersona.AGENT = IssueStreamPersona("agent")
