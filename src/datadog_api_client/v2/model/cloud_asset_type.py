# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class CloudAssetType(ModelSimple):
    """
    The cloud asset type

    :param value: Must be one of ["Host", "HostImage", "Image"].
    :type value: str
    """

    allowed_values = {
        "Host",
        "HostImage",
        "Image",
    }
    HOST: ClassVar["CloudAssetType"]
    HOST_IMAGE: ClassVar["CloudAssetType"]
    IMAGE: ClassVar["CloudAssetType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


CloudAssetType.HOST = CloudAssetType("Host")
CloudAssetType.HOST_IMAGE = CloudAssetType("HostImage")
CloudAssetType.IMAGE = CloudAssetType("Image")
