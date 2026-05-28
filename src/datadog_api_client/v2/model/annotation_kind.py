# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AnnotationKind(ModelSimple):
    """
    Kind of annotation. `pointInTime` annotations mark a single moment in time,
        while `timeRegion` annotations span a window of time and require an `end_time`.

    :param value: Must be one of ["pointInTime", "timeRegion"].
    :type value: str
    """

    allowed_values = {
        "pointInTime",
        "timeRegion",
    }
    POINT_IN_TIME: ClassVar["AnnotationKind"]
    TIME_REGION: ClassVar["AnnotationKind"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AnnotationKind.POINT_IN_TIME = AnnotationKind("pointInTime")
AnnotationKind.TIME_REGION = AnnotationKind("timeRegion")
