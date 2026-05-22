# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SampleLogGenerationDuration(ModelSimple):
    """
    How long the subscription should remain active before expiring.

    :param value: If omitted defaults to "3d". Must be one of ["1h", "1d", "3d", "7d"].
    :type value: str
    """

    allowed_values = {
        "1h",
        "1d",
        "3d",
        "7d",
    }
    ONE_HOUR: ClassVar["SampleLogGenerationDuration"]
    ONE_DAY: ClassVar["SampleLogGenerationDuration"]
    THREE_DAYS: ClassVar["SampleLogGenerationDuration"]
    SEVEN_DAYS: ClassVar["SampleLogGenerationDuration"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SampleLogGenerationDuration.ONE_HOUR = SampleLogGenerationDuration("1h")
SampleLogGenerationDuration.ONE_DAY = SampleLogGenerationDuration("1d")
SampleLogGenerationDuration.THREE_DAYS = SampleLogGenerationDuration("3d")
SampleLogGenerationDuration.SEVEN_DAYS = SampleLogGenerationDuration("7d")
