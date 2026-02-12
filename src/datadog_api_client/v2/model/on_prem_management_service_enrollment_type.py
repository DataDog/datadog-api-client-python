# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class OnPremManagementServiceEnrollmentType(ModelSimple):
    """
    The type of the resource. The value should always be enrollment.

    :param value: If omitted defaults to "enrollment". Must be one of ["enrollment"].
    :type value: str
    """

    allowed_values = {
        "enrollment",
    }
    ENROLLMENT: ClassVar["OnPremManagementServiceEnrollmentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


OnPremManagementServiceEnrollmentType.ENROLLMENT = OnPremManagementServiceEnrollmentType("enrollment")
