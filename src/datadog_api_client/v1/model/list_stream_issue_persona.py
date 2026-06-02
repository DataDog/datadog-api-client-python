# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ListStreamIssuePersona(ModelSimple):
    """
    Persona filter for the `issue_stream` data source.

    :param value: Must be one of ["all", "browser", "mobile", "backend"].
    :type value: str
    """

    allowed_values = {
        "all",
        "browser",
        "mobile",
        "backend",
    }
    ALL: ClassVar["ListStreamIssuePersona"]
    BROWSER: ClassVar["ListStreamIssuePersona"]
    MOBILE: ClassVar["ListStreamIssuePersona"]
    BACKEND: ClassVar["ListStreamIssuePersona"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ListStreamIssuePersona.ALL = ListStreamIssuePersona("all")
ListStreamIssuePersona.BROWSER = ListStreamIssuePersona("browser")
ListStreamIssuePersona.MOBILE = ListStreamIssuePersona("mobile")
ListStreamIssuePersona.BACKEND = ListStreamIssuePersona("backend")
