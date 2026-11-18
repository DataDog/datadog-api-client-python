# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ProductAnalyticsFunnelSuggestionsResponseType(ModelSimple):
    """
    Type of a feature suggestions response.

    :param value: If omitted defaults to "funnel_suggestions_response". Must be one of ["funnel_suggestions_response"].
    :type value: str
    """

    allowed_values = {
        "funnel_suggestions_response",
    }
    FUNNEL_SUGGESTIONS_RESPONSE: ClassVar["ProductAnalyticsFunnelSuggestionsResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ProductAnalyticsFunnelSuggestionsResponseType.FUNNEL_SUGGESTIONS_RESPONSE = (
    ProductAnalyticsFunnelSuggestionsResponseType("funnel_suggestions_response")
)
