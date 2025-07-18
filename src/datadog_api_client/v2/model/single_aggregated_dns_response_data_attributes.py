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
    from datadog_api_client.v2.model.single_aggregated_dns_response_data_attributes_group_by_items import (
        SingleAggregatedDnsResponseDataAttributesGroupByItems,
    )
    from datadog_api_client.v2.model.single_aggregated_dns_response_data_attributes_metrics_items import (
        SingleAggregatedDnsResponseDataAttributesMetricsItems,
    )


class SingleAggregatedDnsResponseDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.single_aggregated_dns_response_data_attributes_group_by_items import (
            SingleAggregatedDnsResponseDataAttributesGroupByItems,
        )
        from datadog_api_client.v2.model.single_aggregated_dns_response_data_attributes_metrics_items import (
            SingleAggregatedDnsResponseDataAttributesMetricsItems,
        )

        return {
            "group_bys": ([SingleAggregatedDnsResponseDataAttributesGroupByItems],),
            "metrics": ([SingleAggregatedDnsResponseDataAttributesMetricsItems],),
        }

    attribute_map = {
        "group_bys": "group_bys",
        "metrics": "metrics",
    }

    def __init__(
        self_,
        group_bys: Union[List[SingleAggregatedDnsResponseDataAttributesGroupByItems], UnsetType] = unset,
        metrics: Union[List[SingleAggregatedDnsResponseDataAttributesMetricsItems], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for an aggregated DNS flow.

        :param group_bys: The key, value pairs for each group by.
        :type group_bys: [SingleAggregatedDnsResponseDataAttributesGroupByItems], optional

        :param metrics: Metrics associated with an aggregated DNS flow.
        :type metrics: [SingleAggregatedDnsResponseDataAttributesMetricsItems], optional
        """
        if group_bys is not unset:
            kwargs["group_bys"] = group_bys
        if metrics is not unset:
            kwargs["metrics"] = metrics
        super().__init__(kwargs)
