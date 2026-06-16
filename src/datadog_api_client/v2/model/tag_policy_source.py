# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TagPolicySource(ModelSimple):
    """
    The telemetry source that a tag policy applies to.

    :param value: Must be one of ["logs", "spans", "metrics", "rum", "feed"].
    :type value: str
    """

    allowed_values = {
        "logs",
        "spans",
        "metrics",
        "rum",
        "feed",
    }
    LOGS: ClassVar["TagPolicySource"]
    SPANS: ClassVar["TagPolicySource"]
    METRICS: ClassVar["TagPolicySource"]
    RUM: ClassVar["TagPolicySource"]
    FEED: ClassVar["TagPolicySource"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TagPolicySource.LOGS = TagPolicySource("logs")
TagPolicySource.SPANS = TagPolicySource("spans")
TagPolicySource.METRICS = TagPolicySource("metrics")
TagPolicySource.RUM = TagPolicySource("rum")
TagPolicySource.FEED = TagPolicySource("feed")
