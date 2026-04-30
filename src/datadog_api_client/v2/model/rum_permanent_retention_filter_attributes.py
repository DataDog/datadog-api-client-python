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
    from datadog_api_client.v2.model.rum_permanent_cross_product_sampling import RumPermanentCrossProductSampling
    from datadog_api_client.v2.model.rum_permanent_cross_product_sampling_editability import (
        RumPermanentCrossProductSamplingEditability,
    )
    from datadog_api_client.v2.model.rum_permanent_retention_filter_event_type import (
        RumPermanentRetentionFilterEventType,
    )


class RumPermanentRetentionFilterAttributes(ModelNormal):
    validations = {
        "sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_permanent_cross_product_sampling import RumPermanentCrossProductSampling
        from datadog_api_client.v2.model.rum_permanent_cross_product_sampling_editability import (
            RumPermanentCrossProductSamplingEditability,
        )
        from datadog_api_client.v2.model.rum_permanent_retention_filter_event_type import (
            RumPermanentRetentionFilterEventType,
        )

        return {
            "cross_product_sampling": (RumPermanentCrossProductSampling,),
            "cross_product_sampling_editability": (RumPermanentCrossProductSamplingEditability,),
            "enabled": (bool,),
            "event_type": (RumPermanentRetentionFilterEventType,),
            "name": (str,),
            "query": (str,),
            "sample_rate": (float,),
        }

    attribute_map = {
        "cross_product_sampling": "cross_product_sampling",
        "cross_product_sampling_editability": "cross_product_sampling_editability",
        "enabled": "enabled",
        "event_type": "event_type",
        "name": "name",
        "query": "query",
        "sample_rate": "sample_rate",
    }

    def __init__(
        self_,
        cross_product_sampling: Union[RumPermanentCrossProductSampling, UnsetType] = unset,
        cross_product_sampling_editability: Union[RumPermanentCrossProductSamplingEditability, UnsetType] = unset,
        enabled: Union[bool, UnsetType] = unset,
        event_type: Union[RumPermanentRetentionFilterEventType, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        query: Union[str, UnsetType] = unset,
        sample_rate: Union[float, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a permanent retention filter.

        :param cross_product_sampling: Cross-product retention settings for a permanent retention filter.
        :type cross_product_sampling: RumPermanentCrossProductSampling, optional

        :param cross_product_sampling_editability: Flags indicating which ``cross_product_sampling`` rates can be updated for this filter. Read-only.
        :type cross_product_sampling_editability: RumPermanentCrossProductSamplingEditability, optional

        :param enabled: Indicates whether the permanent retention filter is active. Read-only.
        :type enabled: bool, optional

        :param event_type: The type of RUM events the filter applies to. Read-only.
        :type event_type: RumPermanentRetentionFilterEventType, optional

        :param name: The name of a permanent retention filter. Read-only.
        :type name: str, optional

        :param query: The query string for a permanent retention filter. Read-only.
        :type query: str, optional

        :param sample_rate: The retention sample rate for a permanent retention filter, from 0 to 100. Read-only.
        :type sample_rate: float, optional
        """
        if cross_product_sampling is not unset:
            kwargs["cross_product_sampling"] = cross_product_sampling
        if cross_product_sampling_editability is not unset:
            kwargs["cross_product_sampling_editability"] = cross_product_sampling_editability
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
