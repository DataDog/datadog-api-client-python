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
    from datadog_api_client.v2.model.rum_cross_product_sampling_update import RUMCrossProductSamplingUpdate
    from datadog_api_client.v2.model.rum_retention_filter_event_type import RUMRetentionFilterEventType


class RUMRetentionFilterUpdateAttributes(ModelNormal):
    validations = {
        "sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0.1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_cross_product_sampling_update import RUMCrossProductSamplingUpdate
        from datadog_api_client.v2.model.rum_retention_filter_event_type import RUMRetentionFilterEventType

        return {
            "cross_product_sampling": (RUMCrossProductSamplingUpdate,),
            "enabled": (bool,),
            "event_type": (RUMRetentionFilterEventType,),
            "name": (str,),
            "query": (str,),
            "sample_rate": (float,),
        }

    attribute_map = {
        "cross_product_sampling": "cross_product_sampling",
        "enabled": "enabled",
        "event_type": "event_type",
        "name": "name",
        "query": "query",
        "sample_rate": "sample_rate",
    }

    def __init__(
        self_,
        cross_product_sampling: Union[RUMCrossProductSamplingUpdate, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        event_type: Union[RUMRetentionFilterEventType, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        sample_rate: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The object describing attributes of a RUM retention filter to update.

        :param cross_product_sampling: The configuration for cross-product retention filters. All fields are optional for partial updates.
        :type cross_product_sampling: RUMCrossProductSamplingUpdate, optional

        :param enabled: Whether the retention filter is enabled.
        :type enabled: bool, optional

        :param event_type: The type of RUM events to filter on.
        :type event_type: RUMRetentionFilterEventType, optional

        :param name: The name of a RUM retention filter.
        :type name: str, optional

        :param query: The query string for a RUM retention filter.
        :type query: str, optional

        :param sample_rate: The sample rate for a RUM retention filter, between 0.1 and 100. Values are truncated to one decimal place.
        :type sample_rate: float, optional
        """
        if cross_product_sampling is not unset:
            kwargs["cross_product_sampling"] = cross_product_sampling
        if enabled is not unset:
            kwargs["enabled"] = enabled
        if event_type is not unset:
            kwargs["event_type"] = event_type
        if name is not unset:
            kwargs["name"] = name
        if query is not unset:
            kwargs["query"] = query
        if sample_rate is not unset:
            kwargs["sample_rate"] = sample_rate
        super().__init__(kwargs)
