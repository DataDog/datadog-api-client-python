# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.timeseries_widget_anomaly_detection_sensitivity import (
        TimeseriesWidgetAnomalyDetectionSensitivity,
    )


class TimeseriesWidgetAnomalyDetection(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.timeseries_widget_anomaly_detection_sensitivity import (
            TimeseriesWidgetAnomalyDetectionSensitivity,
        )

        return {
            "detection_sensitivity": (TimeseriesWidgetAnomalyDetectionSensitivity,),
        }

    attribute_map = {
        "detection_sensitivity": "detection_sensitivity",
    }

    def __init__(self_, detection_sensitivity: TimeseriesWidgetAnomalyDetectionSensitivity, **kwargs):
        """
        Anomaly detection configuration for a timeseries widget.

        :param detection_sensitivity: Sensitivity level for anomaly detection. Use ``never_detect`` to disable anomaly detection.
        :type detection_sensitivity: TimeseriesWidgetAnomalyDetectionSensitivity
        """
        super().__init__(kwargs)

        self_.detection_sensitivity = detection_sensitivity
