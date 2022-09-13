# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class SearchServiceLevelObjective(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_creator import SLOCreator
        from datadog_api_client.v1.model.slo_overall_statuses import SLOOverallStatuses
        from datadog_api_client.v1.model.search_slo_query import SearchSLOQuery
        from datadog_api_client.v1.model.search_slo_threshold import SearchSLOThreshold
        from datadog_api_client.v1.model.slo_type import SLOType

        return {
            "all_tags": ([str],),
            "created_at": (int,),
            "creator": (SLOCreator,),
            "description": (str, none_type),
            "groups": ([str], none_type),
            "id": (str,),
            "modified_at": (int,),
            "monitor_ids": ([int], none_type),
            "name": (str,),
            "overall_status": ([SLOOverallStatuses],),
            "query": (SearchSLOQuery,),
            "thresholds": ([SearchSLOThreshold],),
            "type": (SLOType,),
        }

    attribute_map = {
        "all_tags": "all_tags",
        "created_at": "created_at",
        "creator": "creator",
        "description": "description",
        "groups": "groups",
        "id": "id",
        "modified_at": "modified_at",
        "monitor_ids": "monitor_ids",
        "name": "name",
        "overall_status": "overall_status",
        "query": "query",
        "thresholds": "thresholds",
        "type": "type",
    }
    read_only_vars = {
        "created_at",
        "id",
        "modified_at",
    }

    def __init__(self_, *args, **kwargs):
        """
        A service level objective object includes a service level indicator, thresholds
        for one or more timeframes, and metadata ( ``name`` , ``description`` , ``tags`` , etc.).

        :param all_tags: A list of tags associated with this service level objective.
            Always included in service level objective responses (but may be empty).
            Optional in create/update requests.
        :type all_tags: [str], optional

        :param created_at: Creation timestamp (UNIX time in seconds)

            Always included in service level objective responses.
        :type created_at: int, optional

        :param creator: The creator of the SLO
        :type creator: SLOCreator, none_type, optional

        :param description: A user-defined description of the service level objective.

            Always included in service level objective responses (but may be ``null`` ).
            Optional in create/update requests.
        :type description: str, none_type, optional

        :param groups: A list of (up to 100) monitor groups that narrow the scope of a monitor service level objective.

            Included in service level objective responses if it is not empty. Optional in
            create/update requests for monitor service level objectives, but may only be
            used when then length of the ``monitor_ids`` field is one.
        :type groups: [str], none_type, optional

        :param id: A unique identifier for the service level objective object.

            Always included in service level objective responses.
        :type id: str, optional

        :param modified_at: Modification timestamp (UNIX time in seconds)

            Always included in service level objective responses.
        :type modified_at: int, optional

        :param monitor_ids: A list of monitor ids that defines the scope of a monitor service level
            objective. **Required if type is monitor**.
        :type monitor_ids: [int], none_type, optional

        :param name: The name of the service level objective object.
        :type name: str, optional

        :param overall_status: calculated status and error budget remaining.
        :type overall_status: [SLOOverallStatuses], optional

        :param query: A metric-based SLO. **Required if type is metric**. Note that Datadog only allows the sum by aggregator
            to be used because this will sum up all request counts instead of averaging them, or taking the max or
            min of all of those requests.
        :type query: SearchSLOQuery, none_type, optional

        :param thresholds: The thresholds (timeframes and associated targets) for this service level
            objective object.
        :type thresholds: [SearchSLOThreshold], optional

        :param type: The type of the service level objective.
        :type type: SLOType, optional
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)
