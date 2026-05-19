# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.scorecard_score_data import ScorecardScoreData
    from datadog_api_client.v2.model.list_rules_response_links import ListRulesResponseLinks
    from datadog_api_client.v2.model.list_scorecard_scores_meta import ListScorecardScoresMeta


class ListScorecardScoresResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.scorecard_score_data import ScorecardScoreData
        from datadog_api_client.v2.model.list_rules_response_links import ListRulesResponseLinks
        from datadog_api_client.v2.model.list_scorecard_scores_meta import ListScorecardScoresMeta

        return {
            "data": ([ScorecardScoreData],),
            "links": (ListRulesResponseLinks,),
            "meta": (ListScorecardScoresMeta,),
        }

    attribute_map = {
        "data": "data",
        "links": "links",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[ScorecardScoreData], UnsetType] = unset,
        links: Union[ListRulesResponseLinks, UnsetType] = unset,
        meta: Union[ListScorecardScoresMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        A list of scorecard scores for a given aggregation type.

        :param data: Array of score objects.
        :type data: [ScorecardScoreData], optional

        :param links: Links attributes.
        :type links: ListRulesResponseLinks, optional

        :param meta: Pagination metadata for scores.
        :type meta: ListScorecardScoresMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if links is not unset:
            kwargs["links"] = links
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
