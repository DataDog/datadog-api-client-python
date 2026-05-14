# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IncidentCaseLinkType(ModelSimple):
    """
    Case link resource type.

    :param value: If omitted defaults to "case_link". Must be one of ["case_link"].
    :type value: str
    """

    allowed_values = {
        "case_link",
    }
    CASE_LINK: ClassVar["IncidentCaseLinkType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IncidentCaseLinkType.CASE_LINK = IncidentCaseLinkType("case_link")
