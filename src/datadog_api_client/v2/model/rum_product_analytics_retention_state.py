# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class RUMProductAnalyticsRetentionState(ModelSimple):
    """
    Controls the retention policy for Product Analytics data derived from RUM events.

    :param value: Must be one of ["MAX", "NONE"].
    :type value: str
    """

    allowed_values = {
        "MAX",
        "NONE",
    }
    MAX: ClassVar["RUMProductAnalyticsRetentionState"]
    NONE: ClassVar["RUMProductAnalyticsRetentionState"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


RUMProductAnalyticsRetentionState.MAX = RUMProductAnalyticsRetentionState("MAX")
RUMProductAnalyticsRetentionState.NONE = RUMProductAnalyticsRetentionState("NONE")
