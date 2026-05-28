# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class AnnotationColor(ModelSimple):
    """
    Color used to render the annotation in the UI.

    :param value: Must be one of ["gray", "blue", "purple", "green", "yellow", "red"].
    :type value: str
    """

    allowed_values = {
        "gray",
        "blue",
        "purple",
        "green",
        "yellow",
        "red",
    }
    GRAY: ClassVar["AnnotationColor"]
    BLUE: ClassVar["AnnotationColor"]
    PURPLE: ClassVar["AnnotationColor"]
    GREEN: ClassVar["AnnotationColor"]
    YELLOW: ClassVar["AnnotationColor"]
    RED: ClassVar["AnnotationColor"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


AnnotationColor.GRAY = AnnotationColor("gray")
AnnotationColor.BLUE = AnnotationColor("blue")
AnnotationColor.PURPLE = AnnotationColor("purple")
AnnotationColor.GREEN = AnnotationColor("green")
AnnotationColor.YELLOW = AnnotationColor("yellow")
AnnotationColor.RED = AnnotationColor("red")
