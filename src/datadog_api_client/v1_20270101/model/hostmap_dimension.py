# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class HostmapDimension(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["group", "node", "fill", "size"].
    :type value: str
    """

    allowed_values = {
        "group",
        "node",
        "fill",
        "size",
    }
    GROUP: ClassVar["HostmapDimension"]
    NODE: ClassVar["HostmapDimension"]
    FILL: ClassVar["HostmapDimension"]
    SIZE: ClassVar["HostmapDimension"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


HostmapDimension.GROUP = HostmapDimension("group")
HostmapDimension.NODE = HostmapDimension("node")
HostmapDimension.FILL = HostmapDimension("fill")
HostmapDimension.SIZE = HostmapDimension("size")
