# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SloMeasureMinutes(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["good_minutes", "bad_minutes"].
    :type value: str
    """

    allowed_values = {
        "good_minutes",
        "bad_minutes",
    }
    GOOD_MINUTES: ClassVar["SloMeasureMinutes"]
    BAD_MINUTES: ClassVar["SloMeasureMinutes"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SloMeasureMinutes.GOOD_MINUTES = SloMeasureMinutes("good_minutes")
SloMeasureMinutes.BAD_MINUTES = SloMeasureMinutes("bad_minutes")
