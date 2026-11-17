# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ProductAnalyticsMonitorThresholds(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "critical": (float,),
            "critical_recovery": (float,),
            "warning": (float,),
            "warning_recovery": (float,),
        }

    attribute_map = {
        "critical": "critical",
        "critical_recovery": "critical_recovery",
        "warning": "warning",
        "warning_recovery": "warning_recovery",
    }

    def __init__(
        self_,
        critical: Union[float, UnsetType] = unset,
        critical_recovery: Union[float, UnsetType] = unset,
        warning: Union[float, UnsetType] = unset,
        warning_recovery: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        Alert thresholds of a Product Analytics monitor.
        Keep ``critical`` in sync with the comparison in the monitor query; the query is not derived from these values.

        :param critical: Value that triggers a critical alert.
        :type critical: float, optional

        :param critical_recovery: Value at which a critical alert recovers.
        :type critical_recovery: float, optional

        :param warning: Value that triggers a warning.
        :type warning: float, optional

        :param warning_recovery: Value at which a warning recovers.
        :type warning_recovery: float, optional
        """
        if critical is not unset:
            kwargs["critical"] = critical
        if critical_recovery is not unset:
            kwargs["critical_recovery"] = critical_recovery
        if warning is not unset:
            kwargs["warning"] = warning
        if warning_recovery is not unset:
            kwargs["warning_recovery"] = warning_recovery
        super().__init__(kwargs)
