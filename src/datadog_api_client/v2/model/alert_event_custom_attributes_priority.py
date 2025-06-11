# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AlertEventCustomAttributesPriority(ModelSimple):
    """
    The priority of the alert.

    :param value: If omitted defaults to "5". Must be one of ["1", "2", "3", "4", "5"].
    :type value: str
    """

    allowed_values = {
        "1",
        "2",
        "3",
        "4",
        "5",
    }
    PRIORITY_ONE: ClassVar["AlertEventCustomAttributesPriority"]
    PRIORITY_TWO: ClassVar["AlertEventCustomAttributesPriority"]
    PRIORITY_THREE: ClassVar["AlertEventCustomAttributesPriority"]
    PRIORITY_FOUR: ClassVar["AlertEventCustomAttributesPriority"]
    PRIORITY_FIVE: ClassVar["AlertEventCustomAttributesPriority"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AlertEventCustomAttributesPriority.PRIORITY_ONE = AlertEventCustomAttributesPriority("1")
AlertEventCustomAttributesPriority.PRIORITY_TWO = AlertEventCustomAttributesPriority("2")
AlertEventCustomAttributesPriority.PRIORITY_THREE = AlertEventCustomAttributesPriority("3")
AlertEventCustomAttributesPriority.PRIORITY_FOUR = AlertEventCustomAttributesPriority("4")
AlertEventCustomAttributesPriority.PRIORITY_FIVE = AlertEventCustomAttributesPriority("5")
