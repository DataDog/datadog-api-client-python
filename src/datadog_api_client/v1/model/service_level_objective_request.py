# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
    from datadog_api_client.v1.model.slo_threshold import SLOThreshold
    from datadog_api_client.v1.model.slo_type import SLOType


class ServiceLevelObjectiveRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
        from datadog_api_client.v1.model.slo_threshold import SLOThreshold
        from datadog_api_client.v1.model.slo_type import SLOType

        return {
            "description": (str, none_type),
            "groups": ([str],),
            "monitor_ids": ([int],),
            "name": (str,),
            "query": (ServiceLevelObjectiveQuery,),
            "tags": ([str],),
            "thresholds": ([SLOThreshold],),
            "type": (SLOType,),
        }

    attribute_map = {
        "description": "description",
        "groups": "groups",
        "monitor_ids": "monitor_ids",
        "name": "name",
        "query": "query",
        "tags": "tags",
        "thresholds": "thresholds",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        thresholds: List[SLOThreshold],
        type: SLOType,
        description: Union[str, none_type, UnsetType] = unset,
        groups: Union[List[str], UnsetType] = unset,
        monitor_ids: Union[List[int], UnsetType] = unset,
        query: Union[ServiceLevelObjectiveQuery, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A service level objective object includes a service level indicator, thresholds
        for one or more timeframes, and metadata ( ``name`` , ``description`` , ``tags`` , etc.).

        :param description: A user-defined description of the service level objective.

            Always included in service level objective responses (but may be ``null`` ).
            Optional in create/update requests.
        :type description: str, none_type, optional

        :param groups: A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.

            Included in service level objective responses if it is not empty. Optional in
            create/update requests for monitor service level objectives, but may only be
            used when then length of the ``monitor_ids`` field is one.
        :type groups: [str], optional

        :param monitor_ids: A list of monitor IDs that defines the scope of a monitor service level
            objective. **Required if type is monitor**.
        :type monitor_ids: [int], optional

        :param name: The name of the service level objective object.
        :type name: str

        :param query: A metric-based SLO. **Required if type is metric**. Note that Datadog only allows the sum by aggregator
            to be used because this will sum up all request counts instead of averaging them, or taking the max or
            min of all of those requests.
        :type query: ServiceLevelObjectiveQuery, optional

        :param tags: A list of tags associated with this service level objective.
            Always included in service level objective responses (but may be empty).
            Optional in create/update requests.
        :type tags: [str], optional

        :param thresholds: The thresholds (timeframes and associated targets) for this service level
            objective object.
        :type thresholds: [SLOThreshold]

        :param type: The type of the service level objective.
        :type type: SLOType
        """
        if description is not unset:
            kwargs["description"] = description
        if groups is not unset:
            kwargs["groups"] = groups
        if monitor_ids is not unset:
            kwargs["monitor_ids"] = monitor_ids
        if query is not unset:
            kwargs["query"] = query
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.name = name
        self_.thresholds = thresholds
        self_.type = type
