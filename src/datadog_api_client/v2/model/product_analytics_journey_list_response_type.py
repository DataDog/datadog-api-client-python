# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyListResponseType(ModelSimple):
    """
    The resource type identifier for a journey list response.

    :param value: If omitted defaults to "journey_list_response". Must be one of ["journey_list_response"].
    :type value: str
    """

    allowed_values = {
        "journey_list_response",
    }
    JOURNEY_LIST_RESPONSE: ClassVar["ProductAnalyticsJourneyListResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyListResponseType.JOURNEY_LIST_RESPONSE = ProductAnalyticsJourneyListResponseType(
    "journey_list_response"
)
