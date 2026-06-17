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


class GovernanceInsightAuditCompute(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "aggregation": (str,),
            "interval": (int,),
            "metric": (str,),
            "rollup": (str,),
        }

    attribute_map = {
        "aggregation": "aggregation",
        "interval": "interval",
        "metric": "metric",
        "rollup": "rollup",
    }

    def __init__(self_, aggregation: str, interval: int, metric: str, rollup: Union[str, UnsetType] = unset, **kwargs):
        """
        The aggregation applied to an audit log query.

        :param aggregation: The aggregation function to apply.
        :type aggregation: str

        :param interval: The aggregation time window, in milliseconds.
        :type interval: int

        :param metric: The metric or attribute to aggregate.
        :type metric: str

        :param rollup: An optional secondary aggregation applied to the audit query result.
        :type rollup: str, optional
        """
        if rollup is not unset:
            kwargs["rollup"] = rollup
        super().__init__(kwargs)

        self_.aggregation = aggregation
        self_.interval = interval
        self_.metric = metric
