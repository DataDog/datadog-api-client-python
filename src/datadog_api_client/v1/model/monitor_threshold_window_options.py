# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class MonitorThresholdWindowOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "recovery_window": (str, none_type),
            "trigger_window": (str, none_type),
        }

    attribute_map = {
        "recovery_window": "recovery_window",
        "trigger_window": "trigger_window",
    }

    def __init__(self, *args, **kwargs):
        """
        Alerting time window options.

        :param recovery_window: Describes how long an anomalous metric must be normal before the alert recovers.
        :type recovery_window: str, none_type, optional

        :param trigger_window: Describes how long a metric must be anomalous before an alert triggers.
        :type trigger_window: str, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorThresholdWindowOptions, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
