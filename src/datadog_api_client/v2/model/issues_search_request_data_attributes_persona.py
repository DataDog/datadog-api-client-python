# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssuesSearchRequestDataAttributesPersona(ModelSimple):
    """
    Persona for the search. Either `track` or `persona` must be specified.
        Ignored if `track` is specified.

    :param value: Must be one of ["ALL", "BROWSER", "MOBILE", "BACKEND", "AGENT"].
    :type value: str
    """

    allowed_values = {
        "ALL",
        "BROWSER",
        "MOBILE",
        "BACKEND",
        "AGENT",
    }
    ALL: ClassVar["IssuesSearchRequestDataAttributesPersona"]
    BROWSER: ClassVar["IssuesSearchRequestDataAttributesPersona"]
    MOBILE: ClassVar["IssuesSearchRequestDataAttributesPersona"]
    BACKEND: ClassVar["IssuesSearchRequestDataAttributesPersona"]
    AGENT: ClassVar["IssuesSearchRequestDataAttributesPersona"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuesSearchRequestDataAttributesPersona.ALL = IssuesSearchRequestDataAttributesPersona("ALL")
IssuesSearchRequestDataAttributesPersona.BROWSER = IssuesSearchRequestDataAttributesPersona("BROWSER")
IssuesSearchRequestDataAttributesPersona.MOBILE = IssuesSearchRequestDataAttributesPersona("MOBILE")
IssuesSearchRequestDataAttributesPersona.BACKEND = IssuesSearchRequestDataAttributesPersona("BACKEND")
IssuesSearchRequestDataAttributesPersona.AGENT = IssuesSearchRequestDataAttributesPersona("AGENT")
