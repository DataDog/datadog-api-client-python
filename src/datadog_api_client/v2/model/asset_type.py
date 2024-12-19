# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AssetType(ModelSimple):
    """
    The asset type

    :param value: Must be one of ["Repository", "Service", "Host", "HostImage", "Image"].
    :type value: str
    """

    allowed_values = {
        "Repository",
        "Service",
        "Host",
        "HostImage",
        "Image",
    }
    REPOSITORY: ClassVar["AssetType"]
    SERVICE: ClassVar["AssetType"]
    HOST: ClassVar["AssetType"]
    HOSTIMAGE: ClassVar["AssetType"]
    IMAGE: ClassVar["AssetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AssetType.REPOSITORY = AssetType("Repository")
AssetType.SERVICE = AssetType("Service")
AssetType.HOST = AssetType("Host")
AssetType.HOSTIMAGE = AssetType("HostImage")
AssetType.IMAGE = AssetType("Image")
