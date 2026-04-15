# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsFunnelRequestType(ModelSimple):
    """
    Request type for user journey funnel widget.

    :param value: If omitted defaults to "user_journey_funnel". Must be one of ["user_journey_funnel"].
    :type value: str
    """

    allowed_values = {
        "user_journey_funnel",
    }
    USER_JOURNEY_FUNNEL: ClassVar["ProductAnalyticsFunnelRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsFunnelRequestType.USER_JOURNEY_FUNNEL = ProductAnalyticsFunnelRequestType("user_journey_funnel")
