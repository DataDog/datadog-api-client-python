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
    from datadog_api_client.v2.model.rum_sdk_config_tracing_url_config import RumSdkConfigTracingUrlConfig
    from datadog_api_client.v2.model.rum_sdk_config_match_option import RumSdkConfigMatchOption
    from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_pair import RumSdkConfigDynamicOptionPair
    from datadog_api_client.v2.model.rum_sdk_config_dynamic_option import RumSdkConfigDynamicOption


class RumSdkConfigRumAttributes(ModelNormal):
    validations = {
        "session_replay_sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
        "session_sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
        "trace_sample_rate": {
            "inclusive_maximum": 100,
            "inclusive_minimum": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_sdk_config_tracing_url_config import RumSdkConfigTracingUrlConfig
        from datadog_api_client.v2.model.rum_sdk_config_match_option import RumSdkConfigMatchOption
        from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_pair import RumSdkConfigDynamicOptionPair
        from datadog_api_client.v2.model.rum_sdk_config_dynamic_option import RumSdkConfigDynamicOption

        return {
            "allowed_tracing_urls": ([RumSdkConfigTracingUrlConfig],),
            "allowed_tracking_origins": ([RumSdkConfigMatchOption],),
            "application_id": (str,),
            "context": ([RumSdkConfigDynamicOptionPair],),
            "default_privacy_level": (str,),
            "enable_privacy_for_action_name": (bool,),
            "env": (str,),
            "service": (str,),
            "session_replay_sample_rate": (int,),
            "session_sample_rate": (int,),
            "trace_sample_rate": (int,),
            "track_session_across_subdomains": (bool,),
            "user": ([RumSdkConfigDynamicOptionPair],),
            "version": (RumSdkConfigDynamicOption,),
        }

    attribute_map = {
        "allowed_tracing_urls": "allowed_tracing_urls",
        "allowed_tracking_origins": "allowed_tracking_origins",
        "application_id": "application_id",
        "context": "context",
        "default_privacy_level": "default_privacy_level",
        "enable_privacy_for_action_name": "enable_privacy_for_action_name",
        "env": "env",
        "service": "service",
        "session_replay_sample_rate": "session_replay_sample_rate",
        "session_sample_rate": "session_sample_rate",
        "trace_sample_rate": "trace_sample_rate",
        "track_session_across_subdomains": "track_session_across_subdomains",
        "user": "user",
        "version": "version",
    }

    def __init__(
        self_,
        application_id: str,
        default_privacy_level: str,
        enable_privacy_for_action_name: bool,
        session_replay_sample_rate: int,
        session_sample_rate: int,
        allowed_tracing_urls: Union[List[RumSdkConfigTracingUrlConfig], UnsetType] = unset,
        allowed_tracking_origins: Union[List[RumSdkConfigMatchOption], UnsetType] = unset,
        context: Union[List[RumSdkConfigDynamicOptionPair], UnsetType] = unset,
        env: Union[str, UnsetType] = unset,
        service: Union[str, UnsetType] = unset,
        trace_sample_rate: Union[int, UnsetType] = unset,
        track_session_across_subdomains: Union[bool, UnsetType] = unset,
        user: Union[List[RumSdkConfigDynamicOptionPair], UnsetType] = unset,
        version: Union[RumSdkConfigDynamicOption, UnsetType] = unset,
        **kwargs,
    ):
        """
        The RUM SDK settings for a configuration.

        :param allowed_tracing_urls: A list of URL configurations for distributed tracing.
        :type allowed_tracing_urls: [RumSdkConfigTracingUrlConfig], optional

        :param allowed_tracking_origins: A list of origin patterns allowed for cross-origin session tracking.
        :type allowed_tracking_origins: [RumSdkConfigMatchOption], optional

        :param application_id: The ID of the RUM application this configuration belongs to.
        :type application_id: str

        :param context: A list of dynamic option key-value pairs.
        :type context: [RumSdkConfigDynamicOptionPair], optional

        :param default_privacy_level: The default privacy masking level applied to all RUM data.
        :type default_privacy_level: str

        :param enable_privacy_for_action_name: Whether to mask user-interaction action names for privacy.
        :type enable_privacy_for_action_name: bool

        :param env: The environment tag for the RUM application.
        :type env: str, optional

        :param service: The service name tag for the RUM application.
        :type service: str, optional

        :param session_replay_sample_rate: The percentage of collected sessions for which a replay is captured (0–100).
        :type session_replay_sample_rate: int

        :param session_sample_rate: The percentage of user sessions to collect (0–100).
        :type session_sample_rate: int

        :param trace_sample_rate: The percentage of requests to forward as APM traces (0–100).
        :type trace_sample_rate: int, optional

        :param track_session_across_subdomains: Whether to share a session across subdomains of the same site.
        :type track_session_across_subdomains: bool, optional

        :param user: A list of dynamic option key-value pairs.
        :type user: [RumSdkConfigDynamicOptionPair], optional

        :param version: A dynamic configuration option that extracts a value at runtime using a specified strategy.
        :type version: RumSdkConfigDynamicOption, optional
        """
        if allowed_tracing_urls is not unset:
            kwargs["allowed_tracing_urls"] = allowed_tracing_urls
        if allowed_tracking_origins is not unset:
            kwargs["allowed_tracking_origins"] = allowed_tracking_origins
        if context is not unset:
            kwargs["context"] = context
        if env is not unset:
            kwargs["env"] = env
        if service is not unset:
            kwargs["service"] = service
        if trace_sample_rate is not unset:
            kwargs["trace_sample_rate"] = trace_sample_rate
        if track_session_across_subdomains is not unset:
            kwargs["track_session_across_subdomains"] = track_session_across_subdomains
        if user is not unset:
            kwargs["user"] = user
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.default_privacy_level = default_privacy_level
        self_.enable_privacy_for_action_name = enable_privacy_for_action_name
        self_.session_replay_sample_rate = session_replay_sample_rate
        self_.session_sample_rate = session_sample_rate
