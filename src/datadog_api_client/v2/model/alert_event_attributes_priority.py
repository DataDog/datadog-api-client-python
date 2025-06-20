# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AlertEventAttributesPriority(ModelSimple):
    """
    The priority of the alert.

    :param value: Must be one of ["1", "2", "3", "4", "5"].
    :type value: str
    """

    allowed_values = {
        "1",
        "2",
        "3",
        "4",
        "5",
    }
    PRIORITY_ONE: ClassVar["AlertEventAttributesPriority"]
    PRIORITY_TWO: ClassVar["AlertEventAttributesPriority"]
    PRIORITY_THREE: ClassVar["AlertEventAttributesPriority"]
    PRIORITY_FOUR: ClassVar["AlertEventAttributesPriority"]
    PRIORITY_FIVE: ClassVar["AlertEventAttributesPriority"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AlertEventAttributesPriority.PRIORITY_ONE = AlertEventAttributesPriority("1")
AlertEventAttributesPriority.PRIORITY_TWO = AlertEventAttributesPriority("2")
AlertEventAttributesPriority.PRIORITY_THREE = AlertEventAttributesPriority("3")
AlertEventAttributesPriority.PRIORITY_FOUR = AlertEventAttributesPriority("4")
AlertEventAttributesPriority.PRIORITY_FIVE = AlertEventAttributesPriority("5")
