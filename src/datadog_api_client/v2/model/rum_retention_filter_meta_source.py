# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMRetentionFilterMetaSource(ModelSimple):
    """
    The source of the last update to the retention filter. The value is `unknown` if the request doesn't specify a source.

    :param value: Must be one of ["default", "ui", "terraform", "unknown"].
    :type value: str
    """

    allowed_values = {
        "default",
        "ui",
        "terraform",
        "unknown",
    }
    DEFAULT: ClassVar["RUMRetentionFilterMetaSource"]
    UI: ClassVar["RUMRetentionFilterMetaSource"]
    TERRAFORM: ClassVar["RUMRetentionFilterMetaSource"]
    UNKNOWN: ClassVar["RUMRetentionFilterMetaSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMRetentionFilterMetaSource.DEFAULT = RUMRetentionFilterMetaSource("default")
RUMRetentionFilterMetaSource.UI = RUMRetentionFilterMetaSource("ui")
RUMRetentionFilterMetaSource.TERRAFORM = RUMRetentionFilterMetaSource("terraform")
RUMRetentionFilterMetaSource.UNKNOWN = RUMRetentionFilterMetaSource("unknown")
