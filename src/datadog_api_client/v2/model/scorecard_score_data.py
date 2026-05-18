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
    from datadog_api_client.v2.model.scorecard_score_attributes import ScorecardScoreAttributes
    from datadog_api_client.v2.model.scorecard_score_relationships import ScorecardScoreRelationships
    from datadog_api_client.v2.model.scorecard_score_data_type import ScorecardScoreDataType


class ScorecardScoreData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scorecard_score_attributes import ScorecardScoreAttributes
        from datadog_api_client.v2.model.scorecard_score_relationships import ScorecardScoreRelationships
        from datadog_api_client.v2.model.scorecard_score_data_type import ScorecardScoreDataType

        return {
            "attributes": (ScorecardScoreAttributes,),
            "id": (str,),
            "relationships": (ScorecardScoreRelationships,),
            "type": (ScorecardScoreDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        id: str,
        type: ScorecardScoreDataType,
        attributes: Union[ScorecardScoreAttributes, UnsetType] = unset,
        relationships: Union[ScorecardScoreRelationships, UnsetType] = unset,
        **kwargs,
    ):
        """
        A scorecard score object for a single entity, rule, scorecard, service, or team.

        :param attributes: Attributes of a scorecard score.
        :type attributes: ScorecardScoreAttributes, optional

        :param id: The ID of the entity or resource being scored.
        :type id: str

        :param relationships: Relationships for a scorecard score, depending on the aggregation type.
        :type relationships: ScorecardScoreRelationships, optional

        :param type: The JSON:API resource type.
        :type type: ScorecardScoreDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if relationships is not unset:
            kwargs["relationships"] = relationships
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
