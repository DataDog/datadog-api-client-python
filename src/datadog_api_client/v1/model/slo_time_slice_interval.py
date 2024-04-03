# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SLOTimeSliceInterval(ModelSimple):
    """
    The interval used when querying data, which defines the size of a time slice.
        Two values are allowed: 60 (1 minute) and 300 (5 minutes).
        If not provided, the value defaults to 300 (5 minutes).

    :param value: Must be one of [60, 300].
    :type value: int
    """

    allowed_values = {
        60,
        300,
    }
    ONE_MINUTE: ClassVar["SLOTimeSliceInterval"]
    FIVE_MINUTES: ClassVar["SLOTimeSliceInterval"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (int,),
        }


SLOTimeSliceInterval.ONE_MINUTE = SLOTimeSliceInterval(60)
SLOTimeSliceInterval.FIVE_MINUTES = SLOTimeSliceInterval(300)
