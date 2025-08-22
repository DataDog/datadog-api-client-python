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
    Persona for the search.

    :param value: Must be one of ["browser", "mobile", "backend"].
    :type value: str
    """

    allowed_values = {
        "browser",
        "mobile",
        "backend",
    }
    BROWSER: ClassVar["IssuesSearchRequestDataAttributesPersona"]
    MOBILE: ClassVar["IssuesSearchRequestDataAttributesPersona"]
    BACKEND: ClassVar["IssuesSearchRequestDataAttributesPersona"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuesSearchRequestDataAttributesPersona.BROWSER = IssuesSearchRequestDataAttributesPersona("browser")
IssuesSearchRequestDataAttributesPersona.MOBILE = IssuesSearchRequestDataAttributesPersona("mobile")
IssuesSearchRequestDataAttributesPersona.BACKEND = IssuesSearchRequestDataAttributesPersona("backend")
