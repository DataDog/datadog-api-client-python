# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.llm_obs_patterns_clustered_point_ref import LLMObsPatternsClusteredPointRef


class LLMObsPatternsTopicWithClusteredPoints(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.llm_obs_patterns_clustered_point_ref import LLMObsPatternsClusteredPointRef

        return {
            "cluster_points": ([LLMObsPatternsClusteredPointRef],),
            "coherence_score": (float,),
            "created_at": (datetime,),
            "description": (str,),
            "first_seen_at": (datetime,),
            "hierarchy_level": (int,),
            "id": (str,),
            "is_validated": (bool,),
            "name": (str,),
            "parent_topic_id": (str,),
            "point_count": (int,),
            "run_id": (str,),
        }

    attribute_map = {
        "cluster_points": "cluster_points",
        "coherence_score": "coherence_score",
        "created_at": "created_at",
        "description": "description",
        "first_seen_at": "first_seen_at",
        "hierarchy_level": "hierarchy_level",
        "id": "id",
        "is_validated": "is_validated",
        "name": "name",
        "parent_topic_id": "parent_topic_id",
        "point_count": "point_count",
        "run_id": "run_id",
    }

    def __init__(
        self_,
        coherence_score: float,
        created_at: datetime,
        description: str,
        first_seen_at: datetime,
        hierarchy_level: int,
        id: str,
        is_validated: bool,
        name: str,
        parent_topic_id: str,
        point_count: int,
        run_id: str,
        cluster_points: Union[List[LLMObsPatternsClusteredPointRef], UnsetType] = unset,
        **kwargs,
    ):
        """
        A topic discovered by an LLM Observability patterns run, including the
        clustered points attached to leaf topics.

        :param cluster_points: List of clustered points attached to a topic.
        :type cluster_points: [LLMObsPatternsClusteredPointRef], optional

        :param coherence_score: Coherence score of the topic.
        :type coherence_score: float

        :param created_at: Timestamp when the topic was created.
        :type created_at: datetime

        :param description: Description of the topic.
        :type description: str

        :param first_seen_at: Timestamp when the topic was first seen.
        :type first_seen_at: datetime

        :param hierarchy_level: Level of the topic in the hierarchy. Level 0 is a leaf topic.
        :type hierarchy_level: int

        :param id: Unique identifier of the topic.
        :type id: str

        :param is_validated: Whether the topic has been validated.
        :type is_validated: bool

        :param name: Name of the topic.
        :type name: str

        :param parent_topic_id: Identifier of the parent topic. Empty for top-level topics.
        :type parent_topic_id: str

        :param point_count: Number of data points assigned to the topic.
        :type point_count: int

        :param run_id: Identifier of the run that produced the topic.
        :type run_id: str
        """
        if cluster_points is not unset:
            kwargs["cluster_points"] = cluster_points
        super().__init__(kwargs)

        self_.coherence_score = coherence_score
        self_.created_at = created_at
        self_.description = description
        self_.first_seen_at = first_seen_at
        self_.hierarchy_level = hierarchy_level
        self_.id = id
        self_.is_validated = is_validated
        self_.name = name
        self_.parent_topic_id = parent_topic_id
        self_.point_count = point_count
        self_.run_id = run_id
