# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SLOHistoryResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.slo_history_monitor import SLOHistoryMonitor
        from datadog_api_client.v1.model.slo_history_sli_data import SLOHistorySLIData
        from datadog_api_client.v1.model.slo_history_metrics import SLOHistoryMetrics
        from datadog_api_client.v1.model.slo_threshold import SLOThreshold
        from datadog_api_client.v1.model.slo_type import SLOType
        from datadog_api_client.v1.model.slo_type_numeric import SLOTypeNumeric

        return {
            "from_ts": (int,),
            "group_by": ([str],),
            "groups": ([SLOHistoryMonitor],),
            "monitors": ([SLOHistoryMonitor],),
            "overall": (SLOHistorySLIData,),
            "series": (SLOHistoryMetrics,),
            "thresholds": ({str: (SLOThreshold,)},),
            "to_ts": (int,),
            "type": (SLOType,),
            "type_id": (SLOTypeNumeric,),
        }

    attribute_map = {
        "from_ts": "from_ts",
        "group_by": "group_by",
        "groups": "groups",
        "monitors": "monitors",
        "overall": "overall",
        "series": "series",
        "thresholds": "thresholds",
        "to_ts": "to_ts",
        "type": "type",
        "type_id": "type_id",
    }

    def __init__(self, *args, **kwargs):
        """
        An array of service level objective objects.

        :param from_ts: The ``from`` timestamp in epoch seconds.
        :type from_ts: int, optional

        :param group_by: For ``metric`` based SLOs where the query includes a group-by clause, this represents the list of grouping parameters.

            This is not included in responses for ``monitor`` based SLOs.
        :type group_by: [str], optional

        :param groups: For grouped SLOs, this represents SLI data for specific groups.

            This is not included in the responses for ``metric`` based SLOs.
        :type groups: [SLOHistoryMonitor], optional

        :param monitors: For multi-monitor SLOs, this represents SLI data for specific monitors.

            This is not included in the responses for ``metric`` based SLOs.
        :type monitors: [SLOHistoryMonitor], optional

        :param overall: An object that holds an SLI value and its associated data. It can represent an SLO's overall SLI value.
            This can also represent the SLI value for a specific monitor in multi-monitor SLOs, or a group in grouped SLOs.
        :type overall: SLOHistorySLIData, optional

        :param series: A ``metric`` based SLO history response.

            This is not included in responses for ``monitor`` based SLOs.
        :type series: SLOHistoryMetrics, optional

        :param thresholds: mapping of string timeframe to the SLO threshold.
        :type thresholds: {str: (SLOThreshold,)}, optional

        :param to_ts: The ``to`` timestamp in epoch seconds.
        :type to_ts: int, optional

        :param type: The type of the service level objective.
        :type type: SLOType, optional

        :param type_id: A numeric representation of the type of the service level objective ( ``0`` for
            monitor, ``1`` for metric). Always included in service level objective responses.
            Ignored in create/update requests.
        :type type_id: SLOTypeNumeric, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(SLOHistoryResponseData, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
