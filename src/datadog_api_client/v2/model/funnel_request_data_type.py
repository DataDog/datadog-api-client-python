# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FunnelRequestDataType(ModelSimple):
    """


    :param value: If omitted defaults to "funnel_request". Must be one of ["funnel_request"].
    :type value: str
    """

    allowed_values = {
        "funnel_request",
    }
    FUNNEL_REQUEST: ClassVar["FunnelRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FunnelRequestDataType.FUNNEL_REQUEST = FunnelRequestDataType("funnel_request")
