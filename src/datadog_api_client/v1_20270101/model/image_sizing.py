# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ImageSizing(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["none", "center", "fill", "contain", "cover", "scale-down", "zoom", "fit"].
    :type value: str
    """

    allowed_values = {
        "none",
        "center",
        "fill",
        "contain",
        "cover",
        "scale-down",
        "zoom",
        "fit",
    }
    NONE: ClassVar["ImageSizing"]
    CENTER: ClassVar["ImageSizing"]
    FILL: ClassVar["ImageSizing"]
    CONTAIN: ClassVar["ImageSizing"]
    COVER: ClassVar["ImageSizing"]
    SCALE_DOWN: ClassVar["ImageSizing"]
    ZOOM: ClassVar["ImageSizing"]
    FIT: ClassVar["ImageSizing"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ImageSizing.NONE = ImageSizing("none")
ImageSizing.CENTER = ImageSizing("center")
ImageSizing.FILL = ImageSizing("fill")
ImageSizing.CONTAIN = ImageSizing("contain")
ImageSizing.COVER = ImageSizing("cover")
ImageSizing.SCALE_DOWN = ImageSizing("scale-down")
ImageSizing.ZOOM = ImageSizing("zoom")
ImageSizing.FIT = ImageSizing("fit")
