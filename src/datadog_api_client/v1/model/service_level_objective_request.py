# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


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

    def __init__(self, name, thresholds, type, *args, **kwargs):
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
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.thresholds = thresholds
        self.type = type

    @classmethod
    def _from_openapi_data(cls, name, thresholds, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(ServiceLevelObjectiveRequest, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.name = name
        self.thresholds = thresholds
        self.type = type
        return self
