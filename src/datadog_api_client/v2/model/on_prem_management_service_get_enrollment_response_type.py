# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnPremManagementServiceGetEnrollmentResponseType(ModelSimple):
    """
    The type of the resource. The value should always be getEnrollmentResponse.

    :param value: If omitted defaults to "getEnrollmentResponse". Must be one of ["getEnrollmentResponse"].
    :type value: str
    """

    allowed_values = {
        "getEnrollmentResponse",
    }
    GETENROLLMENTRESPONSE: ClassVar["OnPremManagementServiceGetEnrollmentResponseType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnPremManagementServiceGetEnrollmentResponseType.GETENROLLMENTRESPONSE = (
    OnPremManagementServiceGetEnrollmentResponseType("getEnrollmentResponse")
)
