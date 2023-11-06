# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    StringEnum,
)

from typing import ClassVar


class FreeTextWidgetDefinitionType(StringEnum):
    """
    Type of the free text widget.

    :param value: If omitted defaults to "free_text". Must be one of ["free_text"].
    :type value: str
    """

    allowed_values = {
        "free_text",
    }
    FREE_TEXT: ClassVar["FreeTextWidgetDefinitionType"]


FreeTextWidgetDefinitionType.FREE_TEXT = FreeTextWidgetDefinitionType("free_text")
