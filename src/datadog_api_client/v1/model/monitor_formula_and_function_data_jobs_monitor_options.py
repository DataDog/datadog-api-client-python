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


class MonitorFormulaAndFunctionDataJobsMonitorOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "alert_on_every_failure": (bool,),
        }

    attribute_map = {
        "alert_on_every_failure": "alert_on_every_failure",
    }

    def __init__(self_, alert_on_every_failure: Union[bool, UnsetType] = unset, **kwargs):
        """
        Monitor configuration options for data jobs queries.

        :param alert_on_every_failure: Alert separately for each failed run instead of on the count of trailing failures.
            Only supported for ``failed_runs`` monitors with the ``aastra`` query dialect. It requires
            a ``> 0`` threshold with no warning threshold, an evaluation window of at most two days,
            and renotification disabled.
        :type alert_on_every_failure: bool, optional
        """
        if alert_on_every_failure is not unset:
            kwargs["alert_on_every_failure"] = alert_on_every_failure
        super().__init__(kwargs)
