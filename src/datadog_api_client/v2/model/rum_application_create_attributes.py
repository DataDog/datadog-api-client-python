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
            "create_default_retention_filters": (bool,),
            "name": (str,),
            "product_analytics_retention_state": (RUMProductAnalyticsRetentionState,),
            "rum_event_processing_state": (RUMEventProcessingState,),
            "type": (str,),
        }

    attribute_map = {
        "create_default_retention_filters": "create_default_retention_filters",
        "name": "name",
        "product_analytics_retention_state": "product_analytics_retention_state",
        "rum_event_processing_state": "rum_event_processing_state",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        create_default_retention_filters: Union[bool, UnsetType] = unset,
        product_analytics_retention_state: Union[RUMProductAnalyticsRetentionState, UnsetType] = unset,
        rum_event_processing_state: Union[RUMEventProcessingState, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        RUM application creation attributes.

        :param create_default_retention_filters: Whether to create the default retention filters when the application is created: ``Sessions with errors`` and ``Sessions`` , each with a 100% retention rate.
            Set to ``false`` to create the application without them, for example when you add your own retention filters right after creating it. Until you add retention filters, the application only retains sessions matched by its `permanent retention filters <https://docs.datadoghq.com/real_user_monitoring/rum_without_limits/retention_filters/#permanent-retention-filters>`_.
            This setting doesn't affect permanent retention filters (sessions with forced replays, Synthetics sessions and RUM-APM flat sampling).
        :type create_default_retention_filters: bool, optional

        :param name: Name of the RUM application.
        :type name: str

        :param product_analytics_retention_state: Controls the retention policy for Product Analytics data derived from RUM events.
        :type product_analytics_retention_state: RUMProductAnalyticsRetentionState, optional

        :param rum_event_processing_state: Configures which RUM events are processed and stored for the application.
        :type rum_event_processing_state: RUMEventProcessingState, optional

        :param type: Type of the RUM application. Supported values are ``browser`` , ``ios`` , ``android`` , ``react-native`` , ``flutter`` , ``roku`` , ``electron`` , ``unity`` , ``kotlin-multiplatform``.
        :type type: str, optional
        """
        if create_default_retention_filters is not unset:
            kwargs["create_default_retention_filters"] = create_default_retention_filters
        if product_analytics_retention_state is not unset:
            kwargs["product_analytics_retention_state"] = product_analytics_retention_state
        if rum_event_processing_state is not unset:
            kwargs["rum_event_processing_state"] = rum_event_processing_state
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.name = name
