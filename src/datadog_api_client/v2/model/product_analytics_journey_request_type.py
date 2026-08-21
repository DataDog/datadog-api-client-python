# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsJourneyRequestType(ModelSimple):
    """
    The resource type identifier for a journey funnel request.

    :param value: If omitted defaults to "journey_request". Must be one of ["journey_request"].
    :type value: str
    """

    allowed_values = {
        "journey_request",
    }
    JOURNEY_REQUEST: ClassVar["ProductAnalyticsJourneyRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsJourneyRequestType.JOURNEY_REQUEST = ProductAnalyticsJourneyRequestType("journey_request")
