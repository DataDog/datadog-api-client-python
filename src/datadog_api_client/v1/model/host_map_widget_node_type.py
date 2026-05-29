# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HostMapWidgetNodeType(ModelSimple):
    """
    Which type of infrastructure entity to visualize in the host map.

    :param value: Must be one of ["host", "container", "pod", "cluster"].
    :type value: str
    """

    allowed_values = {
        "host",
        "container",
        "pod",
        "cluster",
    }
    HOST: ClassVar["HostMapWidgetNodeType"]
    CONTAINER: ClassVar["HostMapWidgetNodeType"]
    POD: ClassVar["HostMapWidgetNodeType"]
    CLUSTER: ClassVar["HostMapWidgetNodeType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HostMapWidgetNodeType.HOST = HostMapWidgetNodeType("host")
HostMapWidgetNodeType.CONTAINER = HostMapWidgetNodeType("container")
HostMapWidgetNodeType.POD = HostMapWidgetNodeType("pod")
HostMapWidgetNodeType.CLUSTER = HostMapWidgetNodeType("cluster")
