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
    from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState
    from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState


class RUMApplicationCreateAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState
        from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState

        return {
            "name": (str,),
            "product_analytics_retention_state": (RUMProductAnalyticsRetentionState,),
            "rum_event_processing_state": (RUMEventProcessingState,),
            "type": (str,),
        }

    attribute_map = {
        "name": "name",
        "product_analytics_retention_state": "product_analytics_retention_state",
        "rum_event_processing_state": "rum_event_processing_state",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        product_analytics_retention_state: Union[RUMProductAnalyticsRetentionState, UnsetType] = unset,
        rum_event_processing_state: Union[RUMEventProcessingState, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        RUM application creation attributes.

        :param name: Name of the RUM application.
        :type name: str

        :param product_analytics_retention_state: Controls the retention policy for Product Analytics data derived from RUM events.
        :type product_analytics_retention_state: RUMProductAnalyticsRetentionState, optional

        :param rum_event_processing_state: Configures which RUM events are processed and stored for the application.
        :type rum_event_processing_state: RUMEventProcessingState, optional

        :param type: Type of the RUM application. Supported values are ``browser`` , ``ios`` , ``android`` , ``react-native`` , ``flutter`` , ``roku`` , ``electron`` , ``unity`` , ``kotlin-multiplatform``.
        :type type: str, optional
        """
        if product_analytics_retention_state is not unset:
            kwargs["product_analytics_retention_state"] = product_analytics_retention_state
        if rum_event_processing_state is not unset:
            kwargs["rum_event_processing_state"] = rum_event_processing_state
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.name = name
