# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class MonitorOptions(ModelNormal):
    validations = {
        "min_failure_duration": {
            "inclusive_maximum": 7200,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.monitor_options_aggregation import MonitorOptionsAggregation
        from datadog_api_client.v1.model.monitor_device_id import MonitorDeviceID
        from datadog_api_client.v1.model.monitor_renotify_status_type import MonitorRenotifyStatusType
        from datadog_api_client.v1.model.monitor_threshold_window_options import MonitorThresholdWindowOptions
        from datadog_api_client.v1.model.monitor_thresholds import MonitorThresholds
        from datadog_api_client.v1.model.monitor_formula_and_function_query_definition import (
            MonitorFormulaAndFunctionQueryDefinition,
        )

        return {
            "aggregation": (MonitorOptionsAggregation,),
            "device_ids": ([MonitorDeviceID],),
            "enable_logs_sample": (bool,),
            "escalation_message": (str,),
            "evaluation_delay": (int, none_type),
            "groupby_simple_monitor": (bool,),
            "include_tags": (bool,),
            "locked": (bool,),
            "min_failure_duration": (int, none_type),
            "min_location_failed": (int, none_type),
            "new_group_delay": (int, none_type),
            "new_host_delay": (int, none_type),
            "no_data_timeframe": (int, none_type),
            "notify_audit": (bool,),
            "notify_no_data": (bool,),
            "renotify_interval": (int, none_type),
            "renotify_occurrences": (int, none_type),
            "renotify_statuses": ([MonitorRenotifyStatusType], none_type),
            "require_full_window": (bool,),
            "silenced": (
                {
                    str: (
                        int,
                        none_type,
                    )
                },
            ),
            "synthetics_check_id": (str, none_type),
            "threshold_windows": (MonitorThresholdWindowOptions,),
            "thresholds": (MonitorThresholds,),
            "timeout_h": (int, none_type),
            "variables": ([MonitorFormulaAndFunctionQueryDefinition],),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "device_ids": "device_ids",
        "enable_logs_sample": "enable_logs_sample",
        "escalation_message": "escalation_message",
        "evaluation_delay": "evaluation_delay",
        "groupby_simple_monitor": "groupby_simple_monitor",
        "include_tags": "include_tags",
        "locked": "locked",
        "min_failure_duration": "min_failure_duration",
        "min_location_failed": "min_location_failed",
        "new_group_delay": "new_group_delay",
        "new_host_delay": "new_host_delay",
        "no_data_timeframe": "no_data_timeframe",
        "notify_audit": "notify_audit",
        "notify_no_data": "notify_no_data",
        "renotify_interval": "renotify_interval",
        "renotify_occurrences": "renotify_occurrences",
        "renotify_statuses": "renotify_statuses",
        "require_full_window": "require_full_window",
        "silenced": "silenced",
        "synthetics_check_id": "synthetics_check_id",
        "threshold_windows": "threshold_windows",
        "thresholds": "thresholds",
        "timeout_h": "timeout_h",
        "variables": "variables",
    }
    read_only_vars = {
        "aggregation",
        "device_ids",
    }

    def __init__(self, *args, **kwargs):
        """
        List of options associated with your monitor.

        :param aggregation: Type of aggregation performed in the monitor query.
        :type aggregation: MonitorOptionsAggregation, optional

        :param device_ids: IDs of the device the Synthetics monitor is running on.
        :type device_ids: [MonitorDeviceID], optional

        :param enable_logs_sample: Whether or not to send a log sample when the log monitor triggers.
        :type enable_logs_sample: bool, optional

        :param escalation_message: We recommend using the `is_renotify <https://docs.datadoghq.com/monitors/notify/?tab=is_alert#renotify>`_ ,
            block in the original message instead.
            A message to include with a re-notification. Supports the ``@username`` notification we allow elsewhere.
            Not applicable if ``renotify_interval`` is ``None``.
        :type escalation_message: str, optional

        :param evaluation_delay: Time (in seconds) to delay evaluation, as a non-negative integer. For example, if the value is set to ``300`` (5min),
            the timeframe is set to ``last_5m`` and the time is 7:00, the monitor evaluates data from 6:50 to 6:55.
            This is useful for AWS CloudWatch and other backfilled metrics to ensure the monitor always has data during evaluation.
        :type evaluation_delay: int, none_type, optional

        :param groupby_simple_monitor: Whether the log alert monitor triggers a single alert or multiple alerts when any group breaches a threshold.
        :type groupby_simple_monitor: bool, optional

        :param include_tags: A Boolean indicating whether notifications from this monitor automatically inserts its triggering tags into the title.

            **Examples**


            * If ``True`` , ``[Triggered on {host:h1}] Monitor Title``
            * If ``False`` , ``[Triggered] Monitor Title``
        :type include_tags: bool, optional

        :param locked: Whether or not the monitor is locked (only editable by creator and admins). Use ``restricted_roles`` instead.
        :type locked: bool, optional

        :param min_failure_duration: How long the test should be in failure before alerting (integer, number of seconds, max 7200).
        :type min_failure_duration: int, none_type, optional

        :param min_location_failed: The minimum number of locations in failure at the same time during
            at least one moment in the ``min_failure_duration`` period ( ``min_location_failed`` and ``min_failure_duration``
            are part of the advanced alerting rules - integer, >= 1).
        :type min_location_failed: int, none_type, optional

        :param new_group_delay: Time (in seconds) to skip evaluations for new groups.

            For example, this option can be used to skip evaluations for new hosts while they initialize.

            Must be a non negative integer.
        :type new_group_delay: int, none_type, optional

        :param new_host_delay: Time (in seconds) to allow a host to boot and applications
            to fully start before starting the evaluation of monitor results.
            Should be a non negative integer.

            Use new_group_delay instead.
        :type new_host_delay: int, none_type, optional

        :param no_data_timeframe: The number of minutes before a monitor notifies after data stops reporting.
            Datadog recommends at least 2x the monitor timeframe for query alerts or 2 minutes for service checks.
            If omitted, 2x the evaluation timeframe is used for query alerts, and 24 hours is used for service checks.
        :type no_data_timeframe: int, none_type, optional

        :param notify_audit: A Boolean indicating whether tagged users is notified on changes to this monitor.
        :type notify_audit: bool, optional

        :param notify_no_data: A Boolean indicating whether this monitor notifies when data stops reporting.
        :type notify_no_data: bool, optional

        :param renotify_interval: The number of minutes after the last notification before a monitor re-notifies on the current status.
            It only re-notifies if it’s not resolved.
        :type renotify_interval: int, none_type, optional

        :param renotify_occurrences: The number of times re-notification messages should be sent on the current status at the provided re-notification interval.
        :type renotify_occurrences: int, none_type, optional

        :param renotify_statuses: The types of monitor statuses for which re-notification messages are sent.
        :type renotify_statuses: [MonitorRenotifyStatusType], none_type, optional

        :param require_full_window: A Boolean indicating whether this monitor needs a full window of data before it’s evaluated.
            We highly recommend you set this to ``false`` for sparse metrics,
            otherwise some evaluations are skipped. Default is false.
        :type require_full_window: bool, optional

        :param silenced: Information about the downtime applied to the monitor.
        :type silenced: {str: (int, none_type,)}, optional

        :param synthetics_check_id: ID of the corresponding Synthetic check.
        :type synthetics_check_id: str, none_type, optional

        :param threshold_windows: Alerting time window options.
        :type threshold_windows: MonitorThresholdWindowOptions, optional

        :param thresholds: List of the different monitor threshold available.
        :type thresholds: MonitorThresholds, optional

        :param timeout_h: The number of hours of the monitor not reporting data before it automatically resolves from a triggered state. The minimum allowed value is 0 hours. The maximum allowed value is 24 hours.
        :type timeout_h: int, none_type, optional

        :param variables: List of requests that can be used in the monitor query. **This feature is currently in beta.**
        :type variables: [MonitorFormulaAndFunctionQueryDefinition], optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorOptions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
