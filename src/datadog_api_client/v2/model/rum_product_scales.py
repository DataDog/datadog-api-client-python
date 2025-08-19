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
    from datadog_api_client.v2.model.rum_product_analytics_retention_scale import RUMProductAnalyticsRetentionScale
    from datadog_api_client.v2.model.rum_event_processing_scale import RUMEventProcessingScale


class RUMProductScales(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_product_analytics_retention_scale import RUMProductAnalyticsRetentionScale
        from datadog_api_client.v2.model.rum_event_processing_scale import RUMEventProcessingScale

        return {
            "product_analytics_retention_scale": (RUMProductAnalyticsRetentionScale,),
            "rum_event_processing_scale": (RUMEventProcessingScale,),
        }

    attribute_map = {
        "product_analytics_retention_scale": "product_analytics_retention_scale",
        "rum_event_processing_scale": "rum_event_processing_scale",
    }

    def __init__(
        self_,
        product_analytics_retention_scale: Union[RUMProductAnalyticsRetentionScale, UnsetType] = unset,
        rum_event_processing_scale: Union[RUMEventProcessingScale, UnsetType] = unset,
        **kwargs,
    ):
        """
        Product Scales configuration for the RUM application.

        :param product_analytics_retention_scale: Product Analytics retention scale configuration.
        :type product_analytics_retention_scale: RUMProductAnalyticsRetentionScale, optional

        :param rum_event_processing_scale: RUM event processing scale configuration.
        :type rum_event_processing_scale: RUMEventProcessingScale, optional
        """
        if product_analytics_retention_scale is not unset:
            kwargs["product_analytics_retention_scale"] = product_analytics_retention_scale
        if rum_event_processing_scale is not unset:
            kwargs["rum_event_processing_scale"] = rum_event_processing_scale
        super().__init__(kwargs)
