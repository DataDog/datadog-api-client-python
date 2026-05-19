# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class ScorecardScoresAggregation(ModelSimple):
    """
    Dimension to group scores by.

    :param value: Must be one of ["by-entity", "by-rule", "by-scorecard", "by-team", "by-kind"].
    :type value: str
    """

    allowed_values = {
        "by-entity",
        "by-rule",
        "by-scorecard",
        "by-team",
        "by-kind",
    }
    BY_ENTITY: ClassVar["ScorecardScoresAggregation"]
    BY_RULE: ClassVar["ScorecardScoresAggregation"]
    BY_SCORECARD: ClassVar["ScorecardScoresAggregation"]
    BY_TEAM: ClassVar["ScorecardScoresAggregation"]
    BY_KIND: ClassVar["ScorecardScoresAggregation"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


ScorecardScoresAggregation.BY_ENTITY = ScorecardScoresAggregation("by-entity")
ScorecardScoresAggregation.BY_RULE = ScorecardScoresAggregation("by-rule")
ScorecardScoresAggregation.BY_SCORECARD = ScorecardScoresAggregation("by-scorecard")
ScorecardScoresAggregation.BY_TEAM = ScorecardScoresAggregation("by-team")
ScorecardScoresAggregation.BY_KIND = ScorecardScoresAggregation("by-kind")
