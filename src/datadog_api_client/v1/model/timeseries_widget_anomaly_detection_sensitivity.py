# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TimeseriesWidgetAnomalyDetectionSensitivity(ModelSimple):
    """
    Sensitivity level for anomaly detection. Use `never_detect` to disable anomaly detection.

    :param value: If omitted defaults to "never_detect". Must be one of ["never_detect"].
    :type value: str
    """

    allowed_values = {
        "never_detect",
    }
    NEVER_DETECT: ClassVar["TimeseriesWidgetAnomalyDetectionSensitivity"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TimeseriesWidgetAnomalyDetectionSensitivity.NEVER_DETECT = TimeseriesWidgetAnomalyDetectionSensitivity("never_detect")
