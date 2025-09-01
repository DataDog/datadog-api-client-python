# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class IssuesSearchResultType(ModelSimple):
    """
    Type of the object.

    :param value: If omitted defaults to "error_tracking_search_result". Must be one of ["error_tracking_search_result"].
    :type value: str
    """

    allowed_values = {
        "error_tracking_search_result",
    }
    ERROR_TRACKING_SEARCH_RESULT: ClassVar["IssuesSearchResultType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


IssuesSearchResultType.ERROR_TRACKING_SEARCH_RESULT = IssuesSearchResultType("error_tracking_search_result")
