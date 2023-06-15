# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


from datadog_api_client.v1.model.slo_creator import SLOCreator
from datadog_api_client.v1.model.slo_overall_statuses import SLOOverallStatuses
from datadog_api_client.v1.model.search_slo_query import SearchSLOQuery
from datadog_api_client.v1.model.slo_type import SLOType
from datadog_api_client.v1.model.slo_status import SLOStatus
from datadog_api_client.v1.model.search_slo_threshold import SearchSLOThreshold
from datadog_api_client.v1.model.slo_creator import SLOCreator
from datadog_api_client.v1.model.slo_overall_statuses import SLOOverallStatuses
from datadog_api_client.v1.model.search_slo_query import SearchSLOQuery
from datadog_api_client.v1.model.slo_type import SLOType
from datadog_api_client.v1.model.slo_status import SLOStatus
from datadog_api_client.v1.model.search_slo_threshold import SearchSLOThreshold

if TYPE_CHECKING:
    from datadog_api_client.v1.model.search_service_level_objective_data import SearchServiceLevelObjectiveData


@dataclass
class SearchServiceLevelObjectiveJSON:
    id: str
    all_tags: Union[List[str], UnsetType] = unset
    created_at: Union[int, UnsetType] = unset
    creator: Union[SLOCreator, none_type, UnsetType] = unset
    description: Union[str, none_type, UnsetType] = unset
    env_tags: Union[List[str], UnsetType] = unset
    groups: Union[List[str], none_type, UnsetType] = unset
    modified_at: Union[int, UnsetType] = unset
    monitor_ids: Union[List[int], none_type, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    overall_status: Union[List[SLOOverallStatuses], UnsetType] = unset
    query: Union[SearchSLOQuery, none_type, UnsetType] = unset
    service_tags: Union[List[str], UnsetType] = unset
    slo_type: Union[SLOType, UnsetType] = unset
    status: Union[SLOStatus, UnsetType] = unset
    team_tags: Union[List[str], UnsetType] = unset
    thresholds: Union[List[SearchSLOThreshold], UnsetType] = unset


class SearchServiceLevelObjective(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.search_service_level_objective_data import SearchServiceLevelObjectiveData

        return {
            "data": (SearchServiceLevelObjectiveData,),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = SearchServiceLevelObjectiveJSON

    def __init__(self_, data: Union[SearchServiceLevelObjectiveData, UnsetType] = unset, **kwargs):
        """
        A service level objective data container.

        :param data: A service level objective ID and attributes.
        :type data: SearchServiceLevelObjectiveData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
