# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorStateGroup(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_overall_states import MonitorOverallStates

        return {
            "last_nodata_ts": (int,),
            "last_notified_ts": (int,),
            "last_resolved_ts": (int,),
            "last_triggered_ts": (int,),
            "name": (str,),
            "status": (MonitorOverallStates,),
        }

    attribute_map = {
        "last_nodata_ts": "last_nodata_ts",
        "last_notified_ts": "last_notified_ts",
        "last_resolved_ts": "last_resolved_ts",
        "last_triggered_ts": "last_triggered_ts",
        "name": "name",
        "status": "status",
    }
    read_only_vars = {
        "status",
    }

    def __init__(self, *args, **kwargs):
        """
        Monitor state for a single group.

        :param last_nodata_ts: Latest timestamp the monitor was in NO_DATA state.
        :type last_nodata_ts: int, optional

        :param last_notified_ts: Latest timestamp of the notification sent for this monitor group.
        :type last_notified_ts: int, optional

        :param last_resolved_ts: Latest timestamp the monitor group was resolved.
        :type last_resolved_ts: int, optional

        :param last_triggered_ts: Latest timestamp the monitor group triggered.
        :type last_triggered_ts: int, optional

        :param name: The name of the monitor.
        :type name: str, optional

        :param status: The different states your monitor can be in.
        :type status: MonitorOverallStates, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorStateGroup, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
