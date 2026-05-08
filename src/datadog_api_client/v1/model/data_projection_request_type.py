# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DataProjectionRequestType(ModelSimple):
    """
    Type of a data projection request.

    :param value: If omitted defaults to "data_projection". Must be one of ["data_projection"].
    :type value: str
    """

    allowed_values = {
        "data_projection",
    }
    DATA_PROJECTION: ClassVar["DataProjectionRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DataProjectionRequestType.DATA_PROJECTION = DataProjectionRequestType("data_projection")
