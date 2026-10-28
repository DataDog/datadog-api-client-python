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
    from datadog_api_client.v2.model.rum_product_scales import RUMProductScales


class RUMApplicationAttributes(ModelNormal):
    validations = {
        "api_key_id": {
            "inclusive_maximum": 2147483647,
        },
        "org_id": {
            "inclusive_maximum": 2147483647,
        },
        "product_analytics_replay_sample_rate": {
            "inclusive_maximum": 2147483647,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_product_scales import RUMProductScales

        return {
            "api_key_id": (int,),
            "apm_rum_flat_sampling_replay_enabled": (bool,),
            "apm_rum_flat_sampling_replay_sample_rate": (float,),
            "application_id": (str,),
            "client_token": (str,),
            "created_at": (int,),
            "created_by_handle": (str,),
            "disabled_at": (int,),
            "disabled_by_handle": (str,),
            "error_tracking_exclusion_filter_enabled": (bool,),
            "external_feeds": ([str],),
            "hash": (str,),
            "is_active": (bool,),
            "name": (str,),
            "ootb_metrics_installed": (bool,),
            "org_id": (int,),
            "product_analytics_preview_disabled": (bool,),
            "product_analytics_replay_sample_rate": (int,),
            "product_scales": (RUMProductScales,),
            "remote_config_id": (str,),
            "short_name": (str,),
            "tags": ([str],),
            "type": (str,),
            "updated_at": (int,),
            "updated_by_handle": (str,),
        }

    attribute_map = {
        "api_key_id": "api_key_id",
        "apm_rum_flat_sampling_replay_enabled": "apm_rum_flat_sampling_replay_enabled",
        "apm_rum_flat_sampling_replay_sample_rate": "apm_rum_flat_sampling_replay_sample_rate",
        "application_id": "application_id",
        "client_token": "client_token",
        "created_at": "created_at",
        "created_by_handle": "created_by_handle",
        "disabled_at": "disabled_at",
        "disabled_by_handle": "disabled_by_handle",
        "error_tracking_exclusion_filter_enabled": "error_tracking_exclusion_filter_enabled",
        "external_feeds": "external_feeds",
        "hash": "hash",
        "is_active": "is_active",
        "name": "name",
        "ootb_metrics_installed": "ootb_metrics_installed",
        "org_id": "org_id",
        "product_analytics_preview_disabled": "product_analytics_preview_disabled",
        "product_analytics_replay_sample_rate": "product_analytics_replay_sample_rate",
        "product_scales": "product_scales",
        "remote_config_id": "remote_config_id",
        "short_name": "short_name",
        "tags": "tags",
        "type": "type",
        "updated_at": "updated_at",
        "updated_by_handle": "updated_by_handle",
    }

    def __init__(
        self_,
        application_id: str,
        client_token: str,
        created_at: int,
        created_by_handle: str,
        name: str,
        org_id: int,
        type: str,
        updated_at: int,
        updated_by_handle: str,
        api_key_id: Union[int, UnsetType] = unset,
        apm_rum_flat_sampling_replay_enabled: Union[bool, UnsetType] = unset,
        apm_rum_flat_sampling_replay_sample_rate: Union[float, UnsetType] = unset,
        disabled_at: Union[int, UnsetType] = unset,
        disabled_by_handle: Union[str, UnsetType] = unset,
        error_tracking_exclusion_filter_enabled: Union[bool, UnsetType] = unset,
        external_feeds: Union[List[str], UnsetType] = unset,
        hash: Union[str, UnsetType] = unset,
        is_active: Union[bool, UnsetType] = unset,
        ootb_metrics_installed: Union[bool, UnsetType] = unset,
        product_analytics_preview_disabled: Union[bool, UnsetType] = unset,
        product_analytics_replay_sample_rate: Union[int, UnsetType] = unset,
        product_scales: Union[RUMProductScales, UnsetType] = unset,
        remote_config_id: Union[str, UnsetType] = unset,
        short_name: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        RUM application attributes.

        :param api_key_id: ID of the API key associated with the application.
        :type api_key_id: int, optional

        :param apm_rum_flat_sampling_replay_enabled: Indicates if flat sampling of Session Replay for APM-correlated RUM sessions is enabled.
        :type apm_rum_flat_sampling_replay_enabled: bool, optional

        :param apm_rum_flat_sampling_replay_sample_rate: Sample rate (0-100) of Session Replay for APM-correlated RUM sessions when flat sampling is enabled.
        :type apm_rum_flat_sampling_replay_sample_rate: float, optional

        :param application_id: ID of the RUM application.
        :type application_id: str

        :param client_token: Client token of the RUM application.
        :type client_token: str

        :param created_at: Timestamp in ms of the creation date.
        :type created_at: int

        :param created_by_handle: Handle of the creator user.
        :type created_by_handle: str

        :param disabled_at: Timestamp in ms of the date the RUM application was disabled. Only present if the application was disabled.
        :type disabled_at: int, optional

        :param disabled_by_handle: Handle of the user who disabled the RUM application. Only present if the application was disabled.
        :type disabled_by_handle: str, optional

        :param error_tracking_exclusion_filter_enabled: Indicates if Error Tracking exclusion filters are enabled for the application.
        :type error_tracking_exclusion_filter_enabled: bool, optional

        :param external_feeds: Non-native ingestion paths the RUM application sends its data through. ``otel`` means the application sends RUM data through OpenTelemetry instead of the Datadog RUM SDK.
        :type external_feeds: [str], optional

        :param hash: Hash of the RUM application. Optional.
        :type hash: str, optional

        :param is_active: Indicates if the RUM application is active.
        :type is_active: bool, optional

        :param name: Name of the RUM application.
        :type name: str

        :param ootb_metrics_installed: Indicates if the out-of-the-box RUM metrics are installed for the application.
        :type ootb_metrics_installed: bool, optional

        :param org_id: Org ID of the RUM application.
        :type org_id: int

        :param product_analytics_preview_disabled: Indicates that the Product Analytics preview is disabled for the application. Only present (and ``true`` ) when the Product Analytics retention state is not preview.
        :type product_analytics_preview_disabled: bool, optional

        :param product_analytics_replay_sample_rate: Sample rate (0-100) of Session Replay for Product Analytics sessions.
        :type product_analytics_replay_sample_rate: int, optional

        :param product_scales: Product Scales configuration for the RUM application.
        :type product_scales: RUMProductScales, optional

        :param remote_config_id: ID of the RUM SDK remote configuration for the application, if one exists.
        :type remote_config_id: str, optional

        :param short_name: Short name of the RUM application.
        :type short_name: str, optional

        :param tags: List of tags associated with the RUM application.
        :type tags: [str], optional

        :param type: Type of the RUM application. Possible values are ``browser`` , ``ios`` , ``android`` , ``react-native`` , ``flutter`` , ``roku`` , ``electron`` , ``unity`` , ``kotlin-multiplatform`` , ``react`` , ``nextjs`` , ``angular`` , ``vuejs`` , ``nuxt`` , ``tanstack`` , ``maui`` , ``salesforce-lwc`` , ``shopify`` , ``cpp`` , ``rum-cpp`` , ``unreal``.
        :type type: str

        :param updated_at: Timestamp in ms of the last update date.
        :type updated_at: int

        :param updated_by_handle: Handle of the updater user.
        :type updated_by_handle: str
        """
        if api_key_id is not unset:
            kwargs["api_key_id"] = api_key_id
        if apm_rum_flat_sampling_replay_enabled is not unset:
            kwargs["apm_rum_flat_sampling_replay_enabled"] = apm_rum_flat_sampling_replay_enabled
        if apm_rum_flat_sampling_replay_sample_rate is not unset:
            kwargs["apm_rum_flat_sampling_replay_sample_rate"] = apm_rum_flat_sampling_replay_sample_rate
        if disabled_at is not unset:
            kwargs["disabled_at"] = disabled_at
        if disabled_by_handle is not unset:
            kwargs["disabled_by_handle"] = disabled_by_handle
        if error_tracking_exclusion_filter_enabled is not unset:
            kwargs["error_tracking_exclusion_filter_enabled"] = error_tracking_exclusion_filter_enabled
        if external_feeds is not unset:
            kwargs["external_feeds"] = external_feeds
        if hash is not unset:
            kwargs["hash"] = hash
        if is_active is not unset:
            kwargs["is_active"] = is_active
        if ootb_metrics_installed is not unset:
            kwargs["ootb_metrics_installed"] = ootb_metrics_installed
        if product_analytics_preview_disabled is not unset:
            kwargs["product_analytics_preview_disabled"] = product_analytics_preview_disabled
        if product_analytics_replay_sample_rate is not unset:
            kwargs["product_analytics_replay_sample_rate"] = product_analytics_replay_sample_rate
        if product_scales is not unset:
            kwargs["product_scales"] = product_scales
        if remote_config_id is not unset:
            kwargs["remote_config_id"] = remote_config_id
        if short_name is not unset:
            kwargs["short_name"] = short_name
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.client_token = client_token
        self_.created_at = created_at
        self_.created_by_handle = created_by_handle
        self_.name = name
        self_.org_id = org_id
        self_.type = type
        self_.updated_at = updated_at
        self_.updated_by_handle = updated_by_handle
