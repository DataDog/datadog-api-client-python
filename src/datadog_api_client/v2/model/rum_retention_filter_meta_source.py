# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumRetentionFilterMetaSource(ModelSimple):
    """
    The source of the last change to a RUM retention filter.

    :param value: Must be one of ["default", "ui", "terraform", "unknown"].
    :type value: str
    """

    allowed_values = {
        "default",
        "ui",
        "terraform",
        "unknown",
    }
    DEFAULT: ClassVar["RumRetentionFilterMetaSource"]
    UI: ClassVar["RumRetentionFilterMetaSource"]
    TERRAFORM: ClassVar["RumRetentionFilterMetaSource"]
    UNKNOWN: ClassVar["RumRetentionFilterMetaSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumRetentionFilterMetaSource.DEFAULT = RumRetentionFilterMetaSource("default")
RumRetentionFilterMetaSource.UI = RumRetentionFilterMetaSource("ui")
RumRetentionFilterMetaSource.TERRAFORM = RumRetentionFilterMetaSource("terraform")
RumRetentionFilterMetaSource.UNKNOWN = RumRetentionFilterMetaSource("unknown")
