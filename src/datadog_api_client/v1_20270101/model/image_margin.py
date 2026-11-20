# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    date,
    datetime,
    file_type,
    none_type,
    unset,
    UnsetType,
    UUID,
)

from typing import ClassVar

class ImageMargin(ModelSimple):
    """
    Test-only generated schema for the dashboard versioning proof of concept.

    :param value: Must be one of ["", "sm", "md", "lg", "small", "large"].
    :type value: str
    """

    allowed_values = {
        "",
        "sm",
        "md",
        "lg",
        "small",
        "large",
    }
    : ClassVar["ImageMargin"]
    SM: ClassVar["ImageMargin"]
    MD: ClassVar["ImageMargin"]
    LG: ClassVar["ImageMargin"]
    SMALL: ClassVar["ImageMargin"]
    LARGE: ClassVar["ImageMargin"]



    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }
ImageMargin. = ImageMargin("")
ImageMargin.SM = ImageMargin("sm")
ImageMargin.MD = ImageMargin("md")
ImageMargin.LG = ImageMargin("lg")
ImageMargin.SMALL = ImageMargin("small")
ImageMargin.LARGE = ImageMargin("large")
