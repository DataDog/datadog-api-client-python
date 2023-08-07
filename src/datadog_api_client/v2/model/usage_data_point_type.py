# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UsageDataPointType(ModelSimple):
    """
    The type of shape of the data.

    :param value: If omitted defaults to "usage_data_point". Must be one of ["usage_data_point"].
    :type value: str
    """

    allowed_values = {
        "usage_data_point",
    }
    USAGE_DATA_POINT: ClassVar["UsageDataPointType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UsageDataPointType.USAGE_DATA_POINT = UsageDataPointType("usage_data_point")
