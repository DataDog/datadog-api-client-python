# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyFunnelResponseType(ModelSimple):
    """
    The resource type identifier for a journey funnel response.

    :param value: If omitted defaults to "funnel_response". Must be one of ["funnel_response"].
    :type value: str
    """

    allowed_values = {
        "funnel_response",
    }
    FUNNEL_RESPONSE: ClassVar["ProductAnalyticsJourneyFunnelResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyFunnelResponseType.FUNNEL_RESPONSE = ProductAnalyticsJourneyFunnelResponseType("funnel_response")
