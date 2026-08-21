# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyTimeseriesResponseType(ModelSimple):
    """
    The resource type identifier for a journey timeseries response.

    :param value: If omitted defaults to "journey_timeseries_response". Must be one of ["journey_timeseries_response"].
    :type value: str
    """

    allowed_values = {
        "journey_timeseries_response",
    }
    JOURNEY_TIMESERIES_RESPONSE: ClassVar["ProductAnalyticsJourneyTimeseriesResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyTimeseriesResponseType.JOURNEY_TIMESERIES_RESPONSE = (
    ProductAnalyticsJourneyTimeseriesResponseType("journey_timeseries_response")
)
