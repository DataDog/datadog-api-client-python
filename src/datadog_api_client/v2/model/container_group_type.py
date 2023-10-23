# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ContainerGroupType(ModelSimple):
    """
    Type of container group.

    :param value: If omitted defaults to "container_group". Must be one of ["container_group"].
    :type value: str
    """

    allowed_values = {
        "container_group",
    }
    CONTAINER_GROUP: ClassVar["ContainerGroupType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ContainerGroupType.CONTAINER_GROUP = ContainerGroupType("container_group")
