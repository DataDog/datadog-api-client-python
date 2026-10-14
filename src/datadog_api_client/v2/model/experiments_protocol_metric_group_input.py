# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_protocol_metric_input import ExperimentsProtocolMetricInput


class ExperimentsProtocolMetricGroupInput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_protocol_metric_input import ExperimentsProtocolMetricInput

        return {
            "is_decision": (bool,),
            "metrics": ([ExperimentsProtocolMetricInput], none_type),
            "name": (str,),
        }

    attribute_map = {
        "is_decision": "is_decision",
        "metrics": "metrics",
        "name": "name",
    }

    def __init__(
        self_,
        is_decision: Union[bool, UnsetType] = unset,
        metrics: Union[List[ExperimentsProtocolMetricInput], none_type, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A metric group supplied by the protocol. Empty decision groups are removed.

        :param is_decision: Whether this group contains decision metrics.
        :type is_decision: bool, optional

        :param metrics: Metrics in the group.
        :type metrics: [ExperimentsProtocolMetricInput], none_type, optional

        :param name: Metric group name.
        :type name: str, optional
        """
        if is_decision is not unset:
            kwargs["is_decision"] = is_decision
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
