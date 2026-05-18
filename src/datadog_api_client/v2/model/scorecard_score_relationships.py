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
    from datadog_api_client.v2.model.scorecard_score_relationship_item import ScorecardScoreRelationshipItem


class ScorecardScoreRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scorecard_score_relationship_item import ScorecardScoreRelationshipItem

        return {
            "entity": (ScorecardScoreRelationshipItem,),
            "rule": (ScorecardScoreRelationshipItem,),
            "scorecard": (ScorecardScoreRelationshipItem,),
            "service": (ScorecardScoreRelationshipItem,),
            "team": (ScorecardScoreRelationshipItem,),
        }

    attribute_map = {
        "entity": "entity",
        "rule": "rule",
        "scorecard": "scorecard",
        "service": "service",
        "team": "team",
    }

    def __init__(
        self_,
        entity: Union[ScorecardScoreRelationshipItem, UnsetType] = unset,
        rule: Union[ScorecardScoreRelationshipItem, UnsetType] = unset,
        scorecard: Union[ScorecardScoreRelationshipItem, UnsetType] = unset,
        service: Union[ScorecardScoreRelationshipItem, UnsetType] = unset,
        team: Union[ScorecardScoreRelationshipItem, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships for a scorecard score, depending on the aggregation type.

        :param entity: A relationship item for a score.
        :type entity: ScorecardScoreRelationshipItem, optional

        :param rule: A relationship item for a score.
        :type rule: ScorecardScoreRelationshipItem, optional

        :param scorecard: A relationship item for a score.
        :type scorecard: ScorecardScoreRelationshipItem, optional

        :param service: A relationship item for a score.
        :type service: ScorecardScoreRelationshipItem, optional

        :param team: A relationship item for a score.
        :type team: ScorecardScoreRelationshipItem, optional
        """
        if entity is not unset:
            kwargs["entity"] = entity
        if rule is not unset:
            kwargs["rule"] = rule
        if scorecard is not unset:
            kwargs["scorecard"] = scorecard
        if service is not unset:
            kwargs["service"] = service
        if team is not unset:
            kwargs["team"] = team
        super().__init__(kwargs)
