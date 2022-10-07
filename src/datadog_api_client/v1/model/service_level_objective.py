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
    from datadog_api_client.v1.model.creator import Creator
    from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
    from datadog_api_client.v1.model.slo_threshold import SLOThreshold
    from datadog_api_client.v1.model.slo_type import SLOType


class ServiceLevelObjective(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.creator import Creator
        from datadog_api_client.v1.model.service_level_objective_query import ServiceLevelObjectiveQuery
        from datadog_api_client.v1.model.slo_threshold import SLOThreshold
        from datadog_api_client.v1.model.slo_type import SLOType

        return {
            "created_at": (int,),
            "creator": (Creator,),
            "description": (str, none_type),
            "groups": ([str],),
            "id": (str,),
            "modified_at": (int,),
            "monitor_ids": ([int],),
            "monitor_tags": ([str],),
            "name": (str,),
            "query": (ServiceLevelObjectiveQuery,),
            "tags": ([str],),
            "thresholds": ([SLOThreshold],),
            "type": (SLOType,),
        }

    attribute_map = {
        "created_at": "created_at",
        "creator": "creator",
        "description": "description",
        "groups": "groups",
        "id": "id",
        "modified_at": "modified_at",
        "monitor_ids": "monitor_ids",
        "monitor_tags": "monitor_tags",
        "name": "name",
        "query": "query",
        "tags": "tags",
        "thresholds": "thresholds",
        "type": "type",
    }
    read_only_vars = {
        "created_at",
        "creator",
        "id",
        "modified_at",
    }

    def __init__(
        self_,
        name: str,
        thresholds: List[SLOThreshold],
        type: SLOType,
        created_at: Union[int, UnsetType] = unset,
        creator: Union[Creator, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        groups: Union[List[str], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        modified_at: Union[int, UnsetType] = unset,
        monitor_ids: Union[List[int], UnsetType] = unset,
        monitor_tags: Union[List[str], UnsetType] = unset,
        query: Union[ServiceLevelObjectiveQuery, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        A service level objective object includes a service level indicator, thresholds
        for one or more timeframes, and metadata ( ``name`` , ``description`` , ``tags`` , etc.).

        :param created_at: Creation timestamp (UNIX time in seconds)

            Always included in service level objective responses.
        :type created_at: int, optional

        :param creator: Object describing the creator of the shared element.
        :type creator: Creator, optional

        :param description: A user-defined description of the service level objective.

            Always included in service level objective responses (but may be ``null`` ).
            Optional in create/update requests.
        :type description: str, none_type, optional

        :param groups: A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.

            Included in service level objective responses if it is not empty. Optional in
            create/update requests for monitor service level objectives, but may only be
            used when then length of the ``monitor_ids`` field is one.
        :type groups: [str], optional

        :param id: A unique identifier for the service level objective object.

            Always included in service level objective responses.
        :type id: str, optional

        :param modified_at: Modification timestamp (UNIX time in seconds)

            Always included in service level objective responses.
        :type modified_at: int, optional

        :param monitor_ids: A list of monitor ids that defines the scope of a monitor service level
            objective. **Required if type is monitor**.
        :type monitor_ids: [int], optional

        :param monitor_tags: The union of monitor tags for all monitors referenced by the ``monitor_ids``
            field.
            Always included in service level objective responses for monitor-based service level
            objectives (but may be empty). Ignored in create/update requests. Does not
            affect which monitors are included in the service level objective (that is
            determined entirely by the ``monitor_ids`` field).
        :type monitor_tags: [str], optional

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
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if creator is not unset:
            kwargs["creator"] = creator
        if description is not unset:
            kwargs["description"] = description
        if groups is not unset:
            kwargs["groups"] = groups
        if id is not unset:
            kwargs["id"] = id
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if monitor_ids is not unset:
            kwargs["monitor_ids"] = monitor_ids
        if monitor_tags is not unset:
            kwargs["monitor_tags"] = monitor_tags
        if query is not unset:
            kwargs["query"] = query
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.name = name
        self_.thresholds = thresholds
        self_.type = type
