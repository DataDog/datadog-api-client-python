# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union

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
from datadog_api_client.v1.model.search_service_level_objective_attributes import SearchServiceLevelObjectiveAttributes
from datadog_api_client.v1.model.slo_creator import SLOCreator
from datadog_api_client.v1.model.slo_overall_statuses import SLOOverallStatuses
from datadog_api_client.v1.model.search_slo_query import SearchSLOQuery
from datadog_api_client.v1.model.slo_type import SLOType
from datadog_api_client.v1.model.slo_status import SLOStatus
from datadog_api_client.v1.model.search_slo_threshold import SearchSLOThreshold


@dataclass
class SearchServiceLevelObjectiveDataJSON:
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


class SearchServiceLevelObjectiveData(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attributes": (SearchServiceLevelObjectiveAttributes,),
            "id": (str,),
            "type": (str,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }
    json_api_model = SearchServiceLevelObjectiveDataJSON

    def __init__(
        self_,
        attributes: Union[SearchServiceLevelObjectiveAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A service level objective ID and attributes.

        :param attributes: A service level objective object includes a service level indicator, thresholds
            for one or more timeframes, and metadata ( ``name`` , ``description`` , and ``tags`` ).
        :type attributes: SearchServiceLevelObjectiveAttributes, optional

        :param id: A unique identifier for the service level objective object.

            Always included in service level objective responses.
        :type id: str, optional

        :param type: The type of the object, must be ``slo``.
        :type type: str, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
