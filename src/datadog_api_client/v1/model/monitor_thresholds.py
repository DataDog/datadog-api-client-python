# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class MonitorThresholds(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "critical": (float,),
            "critical_query": (str,),
            "critical_recovery": (float, none_type),
            "critical_recovery_query": (str,),
            "ok": (float, none_type),
            "unknown": (float, none_type),
            "warning": (float, none_type),
            "warning_recovery": (float, none_type),
        }

    attribute_map = {
        "critical": "critical",
        "critical_query": "critical_query",
        "critical_recovery": "critical_recovery",
        "critical_recovery_query": "critical_recovery_query",
        "ok": "ok",
        "unknown": "unknown",
        "warning": "warning",
        "warning_recovery": "warning_recovery",
    }

    def __init__(
        self_,
        critical: Union[float, UnsetType] = unset,
        critical_query: Union[str, UnsetType] = unset,
        critical_recovery: Union[float, none_type, UnsetType] = unset,
        critical_recovery_query: Union[str, UnsetType] = unset,
        ok: Union[float, none_type, UnsetType] = unset,
        unknown: Union[float, none_type, UnsetType] = unset,
        warning: Union[float, none_type, UnsetType] = unset,
        warning_recovery: Union[float, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of the different monitor threshold available.

        :param critical: The monitor ``CRITICAL`` threshold.
        :type critical: float, optional

        :param critical_query: Query evaluated as a dynamic ``CRITICAL`` threshold. Only supported on metric monitors with a formula query and options['variables']. Cannot be combined with static thresholds. This field is in preview.
        :type critical_query: str, optional

        :param critical_recovery: The monitor ``CRITICAL`` recovery threshold.
        :type critical_recovery: float, none_type, optional

        :param critical_recovery_query: Query evaluated as a dynamic ``CRITICAL`` recovery threshold. Only supported on metric monitors with a formula query and options['variables']. Cannot be combined with static thresholds. This field is in preview.
        :type critical_recovery_query: str, optional

        :param ok: The monitor ``OK`` threshold.
        :type ok: float, none_type, optional

        :param unknown: The monitor UNKNOWN threshold.
        :type unknown: float, none_type, optional

        :param warning: The monitor ``WARNING`` threshold.
        :type warning: float, none_type, optional

        :param warning_recovery: The monitor ``WARNING`` recovery threshold.
        :type warning_recovery: float, none_type, optional
        """
        if critical is not unset:
            kwargs["critical"] = critical
        if critical_query is not unset:
            kwargs["critical_query"] = critical_query
        if critical_recovery is not unset:
            kwargs["critical_recovery"] = critical_recovery
        if critical_recovery_query is not unset:
            kwargs["critical_recovery_query"] = critical_recovery_query
        if ok is not unset:
            kwargs["ok"] = ok
        if unknown is not unset:
            kwargs["unknown"] = unknown
        if warning is not unset:
            kwargs["warning"] = warning
        if warning_recovery is not unset:
            kwargs["warning_recovery"] = warning_recovery
        super().__init__(kwargs)
