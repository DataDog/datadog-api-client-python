# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CycloneDXComponentType(ModelSimple):
    """
    The type of the component. Supported types are library, application, and operating-system.

    :param value: Must be one of ["library", "application", "operating-system"].
    :type value: str
    """

    allowed_values = {
        "library",
        "application",
        "operating-system",
    }
    LIBRARY: ClassVar["CycloneDXComponentType"]
    APPLICATION: ClassVar["CycloneDXComponentType"]
    OPERATING_SYSTEM: ClassVar["CycloneDXComponentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CycloneDXComponentType.LIBRARY = CycloneDXComponentType("library")
CycloneDXComponentType.APPLICATION = CycloneDXComponentType("application")
CycloneDXComponentType.OPERATING_SYSTEM = CycloneDXComponentType("operating-system")
