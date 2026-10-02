# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request_data_attributes_metrics_items import (
        ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems,
    )


class ExperimentsPublicProtocolResponseDataAttributesMetricGroupsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_create_metric_collection_v2_request_data_attributes_metrics_items import (
            ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems,
        )

        return {
            "is_decision": (bool,),
            "metrics": ([ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems],),
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
        metrics: Union[List[ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems], UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A group of metrics supplied by the protocol.

        :param is_decision: Whether the group contains decision metrics.
        :type is_decision: bool, optional

        :param metrics: Metrics included in this group.
        :type metrics: [ExperimentsCreateMetricCollectionV2RequestDataAttributesMetricsItems], optional

        :param name: Display name of the metric group.
        :type name: str, optional
        """
        if is_decision is not unset:
            kwargs["is_decision"] = is_decision
        if metrics is not unset:
            kwargs["metrics"] = metrics
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
