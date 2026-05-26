# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AnalysisResponseDataType(ModelSimple):
    """
    Analysis response resource type.

    :param value: If omitted defaults to "server_request". Must be one of ["server_request"].
    :type value: str
    """

    allowed_values = {
        "server_request",
    }
    SERVER_REQUEST: ClassVar["AnalysisResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AnalysisResponseDataType.SERVER_REQUEST = AnalysisResponseDataType("server_request")
