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


class MetricIngestedIndexedVolumeAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "indexed_volume": (int,),
            "indexed_volume_delta": (int,),
            "ingested_volume": (int,),
            "ingested_volume_delta": (int,),
        }

    attribute_map = {
        "indexed_volume": "indexed_volume",
        "indexed_volume_delta": "indexed_volume_delta",
        "ingested_volume": "ingested_volume",
        "ingested_volume_delta": "ingested_volume_delta",
    }

    def __init__(
        self_,
        indexed_volume: Union[int, UnsetType] = unset,
        indexed_volume_delta: Union[int, UnsetType] = unset,
        ingested_volume: Union[int, UnsetType] = unset,
        ingested_volume_delta: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the definition of a metric's ingested and indexed volume.

        :param indexed_volume: Estimated average hourly number of indexed time series for the given metric over the last hour. For organizations on Metric Name Pricing, this represents the estimated sum of indexed data points over the last hour.
        :type indexed_volume: int, optional

        :param indexed_volume_delta: Change in ``indexed_volume`` compared with the previous hour: the last hour's value minus the value for
            the hour before. Negative when volume decreased.
        :type indexed_volume_delta: int, optional

        :param ingested_volume: Estimated average hourly number of ingested time series for the given metric over the last hour. This value is ``0`` for metrics not configured with Metrics Without Limits. For organizations on Metric Name Pricing, this represents the estimated sum of ingested data points over the last hour.
        :type ingested_volume: int, optional

        :param ingested_volume_delta: Change in ``ingested_volume`` compared with the previous hour: the last hour's value minus the value for
            the hour before. Negative when volume decreased.
        :type ingested_volume_delta: int, optional
        """
        if indexed_volume is not unset:
            kwargs["indexed_volume"] = indexed_volume
        if indexed_volume_delta is not unset:
            kwargs["indexed_volume_delta"] = indexed_volume_delta
        if ingested_volume is not unset:
            kwargs["ingested_volume"] = ingested_volume
        if ingested_volume_delta is not unset:
            kwargs["ingested_volume_delta"] = ingested_volume_delta
        super().__init__(kwargs)
