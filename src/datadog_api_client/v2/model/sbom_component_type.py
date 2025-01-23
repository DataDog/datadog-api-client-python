# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SBOMComponentType(ModelSimple):
    """
    The SBOM component type

    :param value: Must be one of ["application", "container", "data", "device", "device-driver", "file", "firmware", "framework", "library", "machine-learning-model", "operating-system", "platform"].
    :type value: str
    """

    allowed_values = {
        "application",
        "container",
        "data",
        "device",
        "device-driver",
        "file",
        "firmware",
        "framework",
        "library",
        "machine-learning-model",
        "operating-system",
        "platform",
    }
    APPLICATION: ClassVar["SBOMComponentType"]
    CONTAINER: ClassVar["SBOMComponentType"]
    DATA: ClassVar["SBOMComponentType"]
    DEVICE: ClassVar["SBOMComponentType"]
    DEVICE_DRIVER: ClassVar["SBOMComponentType"]
    FILE: ClassVar["SBOMComponentType"]
    FIRMWARE: ClassVar["SBOMComponentType"]
    FRAMEWORK: ClassVar["SBOMComponentType"]
    LIBRARY: ClassVar["SBOMComponentType"]
    MACHINE_LEARNING_MODEL: ClassVar["SBOMComponentType"]
    OPERATING_SYSTEM: ClassVar["SBOMComponentType"]
    PLATFORM: ClassVar["SBOMComponentType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SBOMComponentType.APPLICATION = SBOMComponentType("application")
SBOMComponentType.CONTAINER = SBOMComponentType("container")
SBOMComponentType.DATA = SBOMComponentType("data")
SBOMComponentType.DEVICE = SBOMComponentType("device")
SBOMComponentType.DEVICE_DRIVER = SBOMComponentType("device-driver")
SBOMComponentType.FILE = SBOMComponentType("file")
SBOMComponentType.FIRMWARE = SBOMComponentType("firmware")
SBOMComponentType.FRAMEWORK = SBOMComponentType("framework")
SBOMComponentType.LIBRARY = SBOMComponentType("library")
SBOMComponentType.MACHINE_LEARNING_MODEL = SBOMComponentType("machine-learning-model")
SBOMComponentType.OPERATING_SYSTEM = SBOMComponentType("operating-system")
SBOMComponentType.PLATFORM = SBOMComponentType("platform")
