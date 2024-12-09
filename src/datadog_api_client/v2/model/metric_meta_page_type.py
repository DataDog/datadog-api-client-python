# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class MetricMetaPageType(ModelSimple):
    """
    Type of metric pagination.

    :param value: If omitted defaults to "cursor_limit". Must be one of ["cursor_limit"].
    :type value: str
    """

    allowed_values = {
        "cursor_limit",
    }
    CURSOR_LIMIT: ClassVar["MetricMetaPageType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


MetricMetaPageType.CURSOR_LIMIT = MetricMetaPageType("cursor_limit")
