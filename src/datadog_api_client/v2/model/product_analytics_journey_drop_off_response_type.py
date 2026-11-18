# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyDropOffResponseType(ModelSimple):
    """
    The resource type identifier for a journey drop-off analysis response.

    :param value: If omitted defaults to "journey_drop_off_analysis_response". Must be one of ["journey_drop_off_analysis_response"].
    :type value: str
    """

    allowed_values = {
        "journey_drop_off_analysis_response",
    }
    JOURNEY_DROP_OFF_ANALYSIS_RESPONSE: ClassVar["ProductAnalyticsJourneyDropOffResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyDropOffResponseType.JOURNEY_DROP_OFF_ANALYSIS_RESPONSE = (
    ProductAnalyticsJourneyDropOffResponseType("journey_drop_off_analysis_response")
)
