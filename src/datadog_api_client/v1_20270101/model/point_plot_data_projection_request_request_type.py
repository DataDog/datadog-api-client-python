# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class PointPlotDataProjectionRequestRequestType(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: If omitted defaults to "data_projection". Must be one of ["data_projection"].
    :type value: str
    """

    allowed_values = {
        "data_projection",
    }
    DATA_PROJECTION: ClassVar["PointPlotDataProjectionRequestRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


PointPlotDataProjectionRequestRequestType.DATA_PROJECTION = PointPlotDataProjectionRequestRequestType("data_projection")
