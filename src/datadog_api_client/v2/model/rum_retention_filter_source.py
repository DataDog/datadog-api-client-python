# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionFilterSource(ModelSimple):
    """
    The type of RUM events to filter on.

    :param value: Must be one of ["ui", "terraform", "default", "unknown"].
    :type value: str
    """

    allowed_values = {
        "ui",
        "terraform",
        "default",
        "unknown",
    }
    UI: ClassVar["RumRetentionFilterSource"]
    TERRAFORM: ClassVar["RumRetentionFilterSource"]
    DEFAULT: ClassVar["RumRetentionFilterSource"]
    UNKNOWN: ClassVar["RumRetentionFilterSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionFilterSource.UI = RumRetentionFilterSource("ui")
RumRetentionFilterSource.TERRAFORM = RumRetentionFilterSource("terraform")
RumRetentionFilterSource.DEFAULT = RumRetentionFilterSource("default")
RumRetentionFilterSource.UNKNOWN = RumRetentionFilterSource("unknown")
