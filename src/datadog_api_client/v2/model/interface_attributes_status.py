# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class InterfaceAttributesStatus(ModelSimple):
    """
    The interface status

    :param value: Must be one of ["up", "down", "warning", "off"].
    :type value: str
    """

    allowed_values = {
        "up",
        "down",
        "warning",
        "off",
    }
    UP: ClassVar["InterfaceAttributesStatus"]
    DOWN: ClassVar["InterfaceAttributesStatus"]
    WARNING: ClassVar["InterfaceAttributesStatus"]
    OFF: ClassVar["InterfaceAttributesStatus"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


InterfaceAttributesStatus.UP = InterfaceAttributesStatus("up")
InterfaceAttributesStatus.DOWN = InterfaceAttributesStatus("down")
InterfaceAttributesStatus.WARNING = InterfaceAttributesStatus("warning")
InterfaceAttributesStatus.OFF = InterfaceAttributesStatus("off")
