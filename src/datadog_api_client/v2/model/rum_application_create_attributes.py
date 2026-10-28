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
    from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState
    from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState


class RUMApplicationCreateAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 255,
        },
        "product_analytics_replay_sample_rate": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_product_analytics_retention_state import RUMProductAnalyticsRetentionState
        from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState

        return {
            "apm_rum_flat_sampling_replay_enabled": (bool,),
            "apm_rum_flat_sampling_replay_sample_rate": (float,),
            "create_default_retention_filters": (bool,),
            "error_tracking_exclusion_filter_enabled": (bool,),
            "name": (str,),
            "product_analytics_replay_sample_rate": (int,),
            "product_analytics_retention_state": (RUMProductAnalyticsRetentionState,),
            "rum_event_processing_state": (RUMEventProcessingState,),
            "tags": ([str],),
            "type": (str,),
        }

    attribute_map = {
        "apm_rum_flat_sampling_replay_enabled": "apm_rum_flat_sampling_replay_enabled",
        "apm_rum_flat_sampling_replay_sample_rate": "apm_rum_flat_sampling_replay_sample_rate",
        "create_default_retention_filters": "create_default_retention_filters",
        "error_tracking_exclusion_filter_enabled": "error_tracking_exclusion_filter_enabled",
        "name": "name",
        "product_analytics_replay_sample_rate": "product_analytics_replay_sample_rate",
        "product_analytics_retention_state": "product_analytics_retention_state",
        "rum_event_processing_state": "rum_event_processing_state",
        "tags": "tags",
        "type": "type",
    }

    def __init__(
        self_,
        name: str,
        apm_rum_flat_sampling_replay_enabled: Union[bool, UnsetType] = unset,
        apm_rum_flat_sampling_replay_sample_rate: Union[float, UnsetType] = unset,
        create_default_retention_filters: Union[bool, UnsetType] = unset,
        error_tracking_exclusion_filter_enabled: Union[bool, UnsetType] = unset,
        product_analytics_replay_sample_rate: Union[int, UnsetType] = unset,
        product_analytics_retention_state: Union[RUMProductAnalyticsRetentionState, UnsetType] = unset,
        rum_event_processing_state: Union[RUMEventProcessingState, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        RUM application creation attributes.
        When ``rum_event_processing_state`` is omitted, it defaults to ``ALL``. When ``product_analytics_retention_state`` is omitted, Product Analytics is not enabled. Setting it to ``MAX`` requires the ``product_analytics_apps_write`` permission.

        :param apm_rum_flat_sampling_replay_enabled: Indicates if flat sampling of Session Replay for APM-correlated RUM sessions is enabled. Defaults to ``true``.
        :type apm_rum_flat_sampling_replay_enabled: bool, optional

        :param apm_rum_flat_sampling_replay_sample_rate: Sample rate (0-100) of Session Replay for APM-correlated RUM sessions when flat sampling is enabled. Defaults to ``1``.
        :type apm_rum_flat_sampling_replay_sample_rate: float, optional

        :param create_default_retention_filters: Whether to create the default retention filters when the application is created: ``Sessions with errors`` and ``Sessions`` , each with a 100% retention rate.
            Set to ``false`` to create the application without them, for example when you add your own retention filters right after creating it. Until you add retention filters, the application only retains sessions matched by its `permanent retention filters <https://docs.datadoghq.com/real_user_monitoring/rum_without_limits/retention_filters/#permanent-retention-filters>`_.
            This setting doesn't affect permanent retention filters (sessions with forced replays, Synthetics sessions and RUM-APM flat sampling).
        :type create_default_retention_filters: bool, optional

        :param error_tracking_exclusion_filter_enabled: Indicates if Error Tracking exclusion filters are enabled for the application. Defaults to ``false``.
        :type error_tracking_exclusion_filter_enabled: bool, optional

        :param name: Name of the RUM application. Between 1 and 255 characters.
        :type name: str

        :param product_analytics_replay_sample_rate: Sample rate (0-100) of Session Replay for Product Analytics sessions. Defaults to ``100``.
        :type product_analytics_replay_sample_rate: int, optional

        :param product_analytics_retention_state: Controls the retention policy for Product Analytics data derived from RUM events.
            Requests also accept ``PREVIEW`` (the initial state of a new application, reported as ``NONE`` in responses). Setting ``MAX`` requires the ``product_analytics_apps_write`` permission.
        :type product_analytics_retention_state: RUMProductAnalyticsRetentionState, optional

        :param rum_event_processing_state: Configures which RUM events are processed and stored for the application. Defaults to ``ALL`` when creating an application.
        :type rum_event_processing_state: RUMEventProcessingState, optional

        :param tags: List of tags to associate with the RUM application, in ``key:value`` format.
        :type tags: [str], optional

        :param type: Type of the RUM application. Defaults to ``browser``. Supported values are ``browser`` , ``ios`` , ``android`` , ``react-native`` , ``flutter`` , ``roku`` , ``electron`` , ``unity`` , ``kotlin-multiplatform`` , ``react`` , ``nextjs`` , ``angular`` , ``vuejs`` , ``nuxt`` , ``tanstack`` , ``maui`` , ``salesforce-lwc`` , ``shopify`` , ``cpp`` , ``rum-cpp`` , ``unreal``.
        :type type: str, optional
        """
        if apm_rum_flat_sampling_replay_enabled is not unset:
            kwargs["apm_rum_flat_sampling_replay_enabled"] = apm_rum_flat_sampling_replay_enabled
        if apm_rum_flat_sampling_replay_sample_rate is not unset:
            kwargs["apm_rum_flat_sampling_replay_sample_rate"] = apm_rum_flat_sampling_replay_sample_rate
        if create_default_retention_filters is not unset:
            kwargs["create_default_retention_filters"] = create_default_retention_filters
        if error_tracking_exclusion_filter_enabled is not unset:
            kwargs["error_tracking_exclusion_filter_enabled"] = error_tracking_exclusion_filter_enabled
        if product_analytics_replay_sample_rate is not unset:
            kwargs["product_analytics_replay_sample_rate"] = product_analytics_replay_sample_rate
        if product_analytics_retention_state is not unset:
            kwargs["product_analytics_retention_state"] = product_analytics_retention_state
        if rum_event_processing_state is not unset:
            kwargs["rum_event_processing_state"] = rum_event_processing_state
        if tags is not unset:
            kwargs["tags"] = tags
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.name = name
