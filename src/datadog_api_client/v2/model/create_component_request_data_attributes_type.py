# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CreateComponentRequestDataAttributesType(ModelSimple):
    """
    The type of the component.

    :param value: Must be one of ["component", "group"].
    :type value: str
    """

    allowed_values = {
        "component",
        "group",
    }
    COMPONENT: ClassVar["CreateComponentRequestDataAttributesType"]
    GROUP: ClassVar["CreateComponentRequestDataAttributesType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CreateComponentRequestDataAttributesType.COMPONENT = CreateComponentRequestDataAttributesType("component")
CreateComponentRequestDataAttributesType.GROUP = CreateComponentRequestDataAttributesType("group")
