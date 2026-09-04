# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class TimeseriesAnomalyInvestigationInterval(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "end": (int,),
            "start": (int,),
        }

    attribute_map = {
        "end": "end",
        "start": "start",
    }

    def __init__(self_, end: int, start: int, **kwargs):
        """
        Half-open time interval in milliseconds since the Unix epoch.

        :param end: Exclusive end of the interval.
        :type end: int

        :param start: Inclusive start of the interval.
        :type start: int
        """
        super().__init__(kwargs)

        self_.end = end
        self_.start = start
