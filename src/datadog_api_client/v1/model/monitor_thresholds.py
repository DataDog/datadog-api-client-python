# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


class MonitorThresholds(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "critical": (float,),
            "critical_recovery": (float, none_type),
            "ok": (float, none_type),
            "unknown": (float, none_type),
            "warning": (float, none_type),
            "warning_recovery": (float, none_type),
        }

    attribute_map = {
        "critical": "critical",
        "critical_recovery": "critical_recovery",
        "ok": "ok",
        "unknown": "unknown",
        "warning": "warning",
        "warning_recovery": "warning_recovery",
    }

    def __init__(self, *args, **kwargs):
        """
        List of the different monitor threshold available.

        :param critical: The monitor ``CRITICAL`` threshold.
        :type critical: float, optional

        :param critical_recovery: The monitor ``CRITICAL`` recovery threshold.
        :type critical_recovery: float, none_type, optional

        :param ok: The monitor ``OK`` threshold.
        :type ok: float, none_type, optional

        :param unknown: The monitor UNKNOWN threshold.
        :type unknown: float, none_type, optional

        :param warning: The monitor ``WARNING`` threshold.
        :type warning: float, none_type, optional

        :param warning_recovery: The monitor ``WARNING`` recovery threshold.
        :type warning_recovery: float, none_type, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(MonitorThresholds, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
