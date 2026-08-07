# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagRuleSource(ModelSimple):
    """
    The telemetry source that a tag rule applies to.

    :param value: Must be one of ["logs", "spans", "metrics"].
    :type value: str
    """

    allowed_values = {
        "logs",
        "spans",
        "metrics",
    }
    LOGS: ClassVar["TagRuleSource"]
    SPANS: ClassVar["TagRuleSource"]
    METRICS: ClassVar["TagRuleSource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagRuleSource.LOGS = TagRuleSource("logs")
TagRuleSource.SPANS = TagRuleSource("spans")
TagRuleSource.METRICS = TagRuleSource("metrics")
