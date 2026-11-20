# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SloMeasureEvents(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["good_events", "bad_events"].
    :type value: str
    """

    allowed_values = {
        "good_events",
        "bad_events",
    }
    GOOD_EVENTS: ClassVar["SloMeasureEvents"]
    BAD_EVENTS: ClassVar["SloMeasureEvents"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SloMeasureEvents.GOOD_EVENTS = SloMeasureEvents("good_events")
SloMeasureEvents.BAD_EVENTS = SloMeasureEvents("bad_events")
