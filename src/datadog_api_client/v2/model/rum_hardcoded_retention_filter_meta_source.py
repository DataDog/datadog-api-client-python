# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RumHardcodedRetentionFilterMetaSource(ModelSimple):
    """
    The source of the last update to a hardcoded retention filter.

    :param value: Must be one of ["default", "ui", "terraform"].
    :type value: str
    """

    allowed_values = {
        "default",
        "ui",
        "terraform",
    }
    DEFAULT: ClassVar["RumHardcodedRetentionFilterMetaSource"]
    UI: ClassVar["RumHardcodedRetentionFilterMetaSource"]
    TERRAFORM: ClassVar["RumHardcodedRetentionFilterMetaSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RumHardcodedRetentionFilterMetaSource.DEFAULT = RumHardcodedRetentionFilterMetaSource("default")
RumHardcodedRetentionFilterMetaSource.UI = RumHardcodedRetentionFilterMetaSource("ui")
RumHardcodedRetentionFilterMetaSource.TERRAFORM = RumHardcodedRetentionFilterMetaSource("terraform")
