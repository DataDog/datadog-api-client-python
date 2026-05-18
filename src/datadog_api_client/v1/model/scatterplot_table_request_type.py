# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScatterplotTableRequestType(ModelSimple):
    """
    The type of the scatterplot table request.

    :param value: Must be one of ["table", "data_projection"].
    :type value: str
    """

    allowed_values = {
        "table",
        "data_projection",
    }
    TABLE: ClassVar["ScatterplotTableRequestType"]
    DATA_PROJECTION: ClassVar["ScatterplotTableRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScatterplotTableRequestType.TABLE = ScatterplotTableRequestType("table")
ScatterplotTableRequestType.DATA_PROJECTION = ScatterplotTableRequestType("data_projection")
