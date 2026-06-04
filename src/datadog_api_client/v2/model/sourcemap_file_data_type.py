# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class SourcemapFileDataType(ModelSimple):
    """
    The resource type for source map file objects.

    :param value: If omitted defaults to "sourcemap_files". Must be one of ["sourcemap_files"].
    :type value: str
    """

    allowed_values = {
        "sourcemap_files",
    }
    SOURCEMAP_FILES: ClassVar["SourcemapFileDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


SourcemapFileDataType.SOURCEMAP_FILES = SourcemapFileDataType("sourcemap_files")
