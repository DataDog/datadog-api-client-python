# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsFunnelStepSuggestionsRequestType(ModelSimple):
    """
    Type of a step suggestions request.

    :param value: If omitted defaults to "funnel_suggestions_steps_request". Must be one of ["funnel_suggestions_steps_request"].
    :type value: str
    """

    allowed_values = {
        "funnel_suggestions_steps_request",
    }
    FUNNEL_SUGGESTIONS_STEPS_REQUEST: ClassVar["ProductAnalyticsFunnelStepSuggestionsRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsFunnelStepSuggestionsRequestType.FUNNEL_SUGGESTIONS_STEPS_REQUEST = (
    ProductAnalyticsFunnelStepSuggestionsRequestType("funnel_suggestions_steps_request")
)
