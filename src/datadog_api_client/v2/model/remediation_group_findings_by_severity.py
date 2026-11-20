# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RemediationGroupFindingsBySeverity(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "critical": (int,),
            "high": (int,),
            "info": (int,),
            "low": (int,),
            "medium": (int,),
            "none": (int,),
            "unknown": (int,),
        }

    attribute_map = {
        "critical": "critical",
        "high": "high",
        "info": "info",
        "low": "low",
        "medium": "medium",
        "none": "none",
        "unknown": "unknown",
    }

    def __init__(self_, critical: int, high: int, info: int, low: int, medium: int, none: int, unknown: int, **kwargs):
        """
        Number of the group's findings for each value of their ``@severity`` attribute. The response includes every
        level, including levels with a count of zero.

        :param critical: Number of critical findings.
        :type critical: int

        :param high: Number of high findings.
        :type high: int

        :param info: Number of info findings.
        :type info: int

        :param low: Number of low findings.
        :type low: int

        :param medium: Number of medium findings.
        :type medium: int

        :param none: Number of findings with no severity.
        :type none: int

        :param unknown: Number of findings with an unknown severity.
        :type unknown: int
        """
        super().__init__(kwargs)

        self_.critical = critical
        self_.high = high
        self_.info = info
        self_.low = low
        self_.medium = medium
        self_.none = none
        self_.unknown = unknown
