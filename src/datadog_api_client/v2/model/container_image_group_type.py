# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ContainerImageGroupType(ModelSimple):
    """
    Type of Container Image Group.

    :param value: If omitted defaults to "container_image_group". Must be one of ["container_image_group"].
    :type value: str
    """

    allowed_values = {
        "container_image_group",
    }
    CONTAINER_IMAGE_GROUP: ClassVar["ContainerImageGroupType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ContainerImageGroupType.CONTAINER_IMAGE_GROUP = ContainerImageGroupType("container_image_group")
