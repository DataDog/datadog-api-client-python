# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumSegmentSegmentType(ModelSimple):
    """
    The type of a segment based on its data query configuration.

    :param value: Must be one of ["static", "event_platform", "combination", "journeys", "reference_table", "templates"].
    :type value: str
    """

    allowed_values = {
        "static",
        "event_platform",
        "combination",
        "journeys",
        "reference_table",
        "templates",
    }
    STATIC: ClassVar["RumSegmentSegmentType"]
    EVENT_PLATFORM: ClassVar["RumSegmentSegmentType"]
    COMBINATION: ClassVar["RumSegmentSegmentType"]
    JOURNEYS: ClassVar["RumSegmentSegmentType"]
    REFERENCE_TABLE: ClassVar["RumSegmentSegmentType"]
    TEMPLATES: ClassVar["RumSegmentSegmentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumSegmentSegmentType.STATIC = RumSegmentSegmentType("static")
RumSegmentSegmentType.EVENT_PLATFORM = RumSegmentSegmentType("event_platform")
RumSegmentSegmentType.COMBINATION = RumSegmentSegmentType("combination")
RumSegmentSegmentType.JOURNEYS = RumSegmentSegmentType("journeys")
RumSegmentSegmentType.REFERENCE_TABLE = RumSegmentSegmentType("reference_table")
RumSegmentSegmentType.TEMPLATES = RumSegmentSegmentType("templates")
