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
    from datadog_api_client.v2.model.rum_product_analytics_retention_state_request import (
        RUMProductAnalyticsRetentionStateRequest,
    )
    from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState
    from datadog_api_client.v2.model.rum_application_platform_type import RUMApplicationPlatformType


class RUMApplicationUpdateAttributes(ModelNormal):
    validations = {
        "apm_rum_flat_sampling_replay_sample_rate": {
            "inclusive_maximum": 1,
            "inclusive_minimum": 0,
        },
        "name": {
            "max_length": 255,
        },
        "product_analytics_replay_sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_product_analytics_retention_state_request import (
            RUMProductAnalyticsRetentionStateRequest,
        )
        from datadog_api_client.v2.model.rum_event_processing_state import RUMEventProcessingState
        from datadog_api_client.v2.model.rum_application_platform_type import RUMApplicationPlatformType

        return {
            "apm_rum_flat_sampling_replay_enabled": (bool,),
            "apm_rum_flat_sampling_replay_sample_rate": (float,),
            "error_tracking_exclusion_filter_enabled": (bool,),
            "name": (str,),
            "product_analytics_replay_sample_rate": (int,),
            "product_analytics_retention_state": (RUMProductAnalyticsRetentionStateRequest,),
            "remote_config_id": (str,),
            "rum_event_processing_state": (RUMEventProcessingState,),
            "tags": ([str],),
            "type": (RUMApplicationPlatformType,),
        }

    attribute_map = {
        "apm_rum_flat_sampling_replay_enabled": "apm_rum_flat_sampling_replay_enabled",
        "apm_rum_flat_sampling_replay_sample_rate": "apm_rum_flat_sampling_replay_sample_rate",
        "error_tracking_exclusion_filter_enabled": "error_tracking_exclusion_filter_enabled",
        "name": "name",
        "product_analytics_replay_sample_rate": "product_analytics_replay_sample_rate",
        "product_analytics_retention_state": "product_analytics_retention_state",
        "remote_config_id": "remote_config_id",
        "rum_event_processing_state": "rum_event_processing_state",
        "tags": "tags",
        "type": "type",
    }

    def __init__(
        self_,
        apm_rum_flat_sampling_replay_enabled: Union[bool, UnsetType] = unset,
        apm_rum_flat_sampling_replay_sample_rate: Union[float, UnsetType] = unset,
        error_tracking_exclusion_filter_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        product_analytics_replay_sample_rate: Union[int, UnsetType] = unset,
        product_analytics_retention_state: Union[RUMProductAnalyticsRetentionStateRequest, UnsetType] = unset,
        remote_config_id: Union[str, UnsetType] = unset,
        rum_event_processing_state: Union[RUMEventProcessingState, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        type: Union[RUMApplicationPlatformType, UnsetType] = unset,
        **kwargs,
    ):
        """
        RUM application update attributes. Only the attributes you provide are changed. Omitted attributes keep their current value.
        Changing ``product_analytics_retention_state`` or ``product_analytics_replay_sample_rate`` requires the ``product_analytics_apps_write`` permission.

        :param apm_rum_flat_sampling_replay_enabled: Whether flat sampling of Session Replay for APM-correlated RUM sessions is enabled.
        :type apm_rum_flat_sampling_replay_enabled: bool, optional

        :param apm_rum_flat_sampling_replay_sample_rate: Fraction (0 to 1) of APM-correlated RUM sessions with Session Replay when flat sampling is enabled.
        :type apm_rum_flat_sampling_replay_sample_rate: float, optional

        :param error_tracking_exclusion_filter_enabled: Whether Error Tracking exclusion filters are enabled for the application.
        :type error_tracking_exclusion_filter_enabled: bool, optional

        :param name: New name of the RUM application. Between 1 and 255 characters.
        :type name: str, optional

        :param product_analytics_replay_sample_rate: Sample rate (0-100) of Session Replay for Product Analytics sessions.
        :type product_analytics_replay_sample_rate: int, optional

        :param product_analytics_retention_state: Retention policy to set for Product Analytics data derived from RUM events. ``PREVIEW`` is the initial state of a new application and is reported as ``NONE`` in responses. Setting ``MAX`` requires the ``product_analytics_apps_write`` permission.
        :type product_analytics_retention_state: RUMProductAnalyticsRetentionStateRequest, optional

        :param remote_config_id: ID of the RUM SDK remote configuration to associate with the application.
        :type remote_config_id: str, optional

        :param rum_event_processing_state: Configures which RUM events are processed and stored for the application. Defaults to ``ALL`` when creating an application.
        :type rum_event_processing_state: RUMEventProcessingState, optional

        :param tags: New list of tags for the RUM application, in ``key:value`` format. Replaces the existing tags.
        :type tags: [str], optional

        :param type: Type of the RUM application, that is the platform of the RUM SDK. Defaults to ``browser`` on create.
        :type type: RUMApplicationPlatformType, optional
        """
        if apm_rum_flat_sampling_replay_enabled is not unset:
            kwargs["apm_rum_flat_sampling_replay_enabled"] = apm_rum_flat_sampling_replay_enabled
        if apm_rum_flat_sampling_replay_sample_rate is not unset:
            kwargs["apm_rum_flat_sampling_replay_sample_rate"] = apm_rum_flat_sampling_replay_sample_rate
        if error_tracking_exclusion_filter_enabled is not unset:
            kwargs["error_tracking_exclusion_filter_enabled"] = error_tracking_exclusion_filter_enabled
        if name is not unset:
            kwargs["name"] = name
        if product_analytics_replay_sample_rate is not unset:
            kwargs["product_analytics_replay_sample_rate"] = product_analytics_replay_sample_rate
        if product_analytics_retention_state is not unset:
            kwargs["product_analytics_retention_state"] = product_analytics_retention_state
        if remote_config_id is not unset:
            kwargs["remote_config_id"] = remote_config_id
        if rum_event_processing_state is not unset:
            kwargs["rum_event_processing_state"] = rum_event_processing_state
        if tags is not unset:
            kwargs["tags"] = tags
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
