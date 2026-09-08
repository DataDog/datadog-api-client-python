# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TimeseriesAnomalyInvestigationMaximumDeviation(ModelNormal):
    validations = {
        "delta_from_boundary": {
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "delta_from_boundary": (float,),
            "timestamp": (int,),
            "value": (float,),
        }

    attribute_map = {
        "delta_from_boundary": "delta_from_boundary",
        "timestamp": "timestamp",
        "value": "value",
    }

    def __init__(self_, delta_from_boundary: float, timestamp: int, value: float, **kwargs):
        """
        Most anomalous point within the detected interval.

        :param delta_from_boundary: Absolute distance between the observed value and the nearest anomaly boundary.
        :type delta_from_boundary: float

        :param timestamp: Point timestamp in milliseconds since the Unix epoch.
        :type timestamp: int

        :param value: Observed value at the point.
        :type value: float
        """
        super().__init__(kwargs)

        self_.delta_from_boundary = delta_from_boundary
        self_.timestamp = timestamp
        self_.value = value
