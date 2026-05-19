# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.scorecard_scores_aggregation import ScorecardScoresAggregation


class ScorecardScoreAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scorecard_scores_aggregation import ScorecardScoresAggregation

        return {
            "aggregation": (ScorecardScoresAggregation,),
            "denominator": (int,),
            "level": (int,),
            "numerator": (int,),
            "score": (float,),
            "total_entities": (int,),
            "total_fail": (int,),
            "total_no_data": (int,),
            "total_pass": (int,),
            "total_skip": (int,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "denominator": "denominator",
        "level": "level",
        "numerator": "numerator",
        "score": "score",
        "total_entities": "total_entities",
        "total_fail": "total_fail",
        "total_no_data": "total_no_data",
        "total_pass": "total_pass",
        "total_skip": "total_skip",
    }

    def __init__(
        self_,
        aggregation: Union[ScorecardScoresAggregation, UnsetType] = unset,
        denominator: Union[int, UnsetType] = unset,
        level: Union[int, UnsetType] = unset,
        numerator: Union[int, UnsetType] = unset,
        score: Union[float, UnsetType] = unset,
        total_entities: Union[int, UnsetType] = unset,
        total_fail: Union[int, UnsetType] = unset,
        total_no_data: Union[int, UnsetType] = unset,
        total_pass: Union[int, UnsetType] = unset,
        total_skip: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a scorecard score.

        :param aggregation: Dimension to group scores by.
        :type aggregation: ScorecardScoresAggregation, optional

        :param denominator: The denominator used to compute the score ratio.
        :type denominator: int, optional

        :param level: The maturity level of the associated rule.
        :type level: int, optional

        :param numerator: The numerator used to compute the score ratio.
        :type numerator: int, optional

        :param score: The computed score ratio (numerator/denominator), from 0 to 1.
        :type score: float, optional

        :param total_entities: The total number of entities evaluated.
        :type total_entities: int, optional

        :param total_fail: The number of rules that failed.
        :type total_fail: int, optional

        :param total_no_data: The number of rules with no data.
        :type total_no_data: int, optional

        :param total_pass: The number of rules that passed.
        :type total_pass: int, optional

        :param total_skip: The number of rules that were skipped.
        :type total_skip: int, optional
        """
        if aggregation is not unset:
            kwargs["aggregation"] = aggregation
        if denominator is not unset:
            kwargs["denominator"] = denominator
        if level is not unset:
            kwargs["level"] = level
        if numerator is not unset:
            kwargs["numerator"] = numerator
        if score is not unset:
            kwargs["score"] = score
        if total_entities is not unset:
            kwargs["total_entities"] = total_entities
        if total_fail is not unset:
            kwargs["total_fail"] = total_fail
        if total_no_data is not unset:
            kwargs["total_no_data"] = total_no_data
        if total_pass is not unset:
            kwargs["total_pass"] = total_pass
        if total_skip is not unset:
            kwargs["total_skip"] = total_skip
        super().__init__(kwargs)
