# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dns_metric_key import DnsMetricKey


class SingleAggregatedDnsResponseDataAttributesMetricsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dns_metric_key import DnsMetricKey

        return {
            "key": (DnsMetricKey,),
            "value": (int,),
        }

    attribute_map = {
        "key": "key",
        "value": "value",
    }

    def __init__(self_, key: Union[DnsMetricKey, UnsetType] = unset, value: Union[int, UnsetType] = unset, **kwargs):
        """
        Metrics associated with an aggregated DNS flow.

        :param key: The metric key for DNS metrics.
        :type key: DnsMetricKey, optional

        :param value: The metric value.
        :type value: int, optional
        """
        if key is not unset:
            kwargs["key"] = key
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
