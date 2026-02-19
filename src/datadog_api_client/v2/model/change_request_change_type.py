# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ChangeRequestChangeType(ModelSimple):
    """
    The type of the change request.

    :param value: Must be one of ["NORMAL", "STANDARD", "EMERGENCY"].
    :type value: str
    """

    allowed_values = {
        "NORMAL",
        "STANDARD",
        "EMERGENCY",
    }
    NORMAL: ClassVar["ChangeRequestChangeType"]
    STANDARD: ClassVar["ChangeRequestChangeType"]
    EMERGENCY: ClassVar["ChangeRequestChangeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ChangeRequestChangeType.NORMAL = ChangeRequestChangeType("NORMAL")
ChangeRequestChangeType.STANDARD = ChangeRequestChangeType("STANDARD")
ChangeRequestChangeType.EMERGENCY = ChangeRequestChangeType("EMERGENCY")
