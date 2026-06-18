"""
Update a RUM SDK configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_remote_config_api import RUMRemoteConfigApi
from datadog_api_client.v2.model.rum_sdk_config_dynamic_option import RumSdkConfigDynamicOption
from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_pair import RumSdkConfigDynamicOptionPair
from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_serialized_type import (
    RumSdkConfigDynamicOptionSerializedType,
)
from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_strategy import RumSdkConfigDynamicOptionStrategy
from datadog_api_client.v2.model.rum_sdk_config_match_option import RumSdkConfigMatchOption
from datadog_api_client.v2.model.rum_sdk_config_match_option_serialized_type import (
    RumSdkConfigMatchOptionSerializedType,
)
from datadog_api_client.v2.model.rum_sdk_config_rum_update_attributes import RumSdkConfigRumUpdateAttributes
from datadog_api_client.v2.model.rum_sdk_config_serialized_regex import RumSdkConfigSerializedRegex
from datadog_api_client.v2.model.rum_sdk_config_serialized_regex_type import RumSdkConfigSerializedRegexType
from datadog_api_client.v2.model.rum_sdk_config_tracing_url_config import RumSdkConfigTracingUrlConfig
from datadog_api_client.v2.model.rum_sdk_config_tracing_url_propagator_type import RumSdkConfigTracingUrlPropagatorType
from datadog_api_client.v2.model.rum_sdk_config_type import RumSdkConfigType
from datadog_api_client.v2.model.rum_sdk_config_update_attributes import RumSdkConfigUpdateAttributes
from datadog_api_client.v2.model.rum_sdk_config_update_data import RumSdkConfigUpdateData
from datadog_api_client.v2.model.rum_sdk_config_update_request import RumSdkConfigUpdateRequest

body = RumSdkConfigUpdateRequest(
    data=RumSdkConfigUpdateData(
        attributes=RumSdkConfigUpdateAttributes(
            rum=RumSdkConfigRumUpdateAttributes(
                allowed_tracing_urls=[
                    RumSdkConfigTracingUrlConfig(
                        match=RumSdkConfigMatchOption(
                            rc_serialized_type=RumSdkConfigMatchOptionSerializedType.STRING,
                            value="https://app.datadoghq.com",
                        ),
                        propagator_types=[
                            RumSdkConfigTracingUrlPropagatorType.DATADOG,
                            RumSdkConfigTracingUrlPropagatorType.TRACECONTEXT,
                        ],
                    ),
                ],
                allowed_tracking_origins=[
                    RumSdkConfigMatchOption(
                        rc_serialized_type=RumSdkConfigMatchOptionSerializedType.STRING,
                        value="https://app.datadoghq.com",
                    ),
                ],
                context=[
                    RumSdkConfigDynamicOptionPair(
                        key="id",
                        value=RumSdkConfigDynamicOption(
                            attribute="data-version",
                            extractor=RumSdkConfigSerializedRegex(
                                rc_serialized_type=RumSdkConfigSerializedRegexType.REGEX,
                                value="^https://app-.*.datadoghq.com",
                            ),
                            key="app.version",
                            name="app_version",
                            path="application.version",
                            rc_serialized_type=RumSdkConfigDynamicOptionSerializedType.DYNAMIC,
                            selector="#app-version",
                            strategy=RumSdkConfigDynamicOptionStrategy.JS,
                        ),
                    ),
                ],
                default_privacy_level="mask",
                enable_privacy_for_action_name=True,
                env="production",
                service="my-service",
                session_replay_sample_rate=20,
                session_sample_rate=75,
                trace_sample_rate=100,
                track_session_across_subdomains=False,
                user=[
                    RumSdkConfigDynamicOptionPair(
                        key="id",
                        value=RumSdkConfigDynamicOption(
                            attribute="data-version",
                            extractor=RumSdkConfigSerializedRegex(
                                rc_serialized_type=RumSdkConfigSerializedRegexType.REGEX,
                                value="^https://app-.*.datadoghq.com",
                            ),
                            key="app.version",
                            name="app_version",
                            path="application.version",
                            rc_serialized_type=RumSdkConfigDynamicOptionSerializedType.DYNAMIC,
                            selector="#app-version",
                            strategy=RumSdkConfigDynamicOptionStrategy.JS,
                        ),
                    ),
                ],
                version=RumSdkConfigDynamicOption(
                    attribute="data-version",
                    extractor=RumSdkConfigSerializedRegex(
                        rc_serialized_type=RumSdkConfigSerializedRegexType.REGEX,
                        value="^https://app-.*.datadoghq.com",
                    ),
                    key="app.version",
                    name="app_version",
                    path="application.version",
                    rc_serialized_type=RumSdkConfigDynamicOptionSerializedType.DYNAMIC,
                    selector="#app-version",
                    strategy=RumSdkConfigDynamicOptionStrategy.JS,
                ),
            ),
        ),
        id="abc12345-1234-5678-abcd-ef1234567890",
        type=RumSdkConfigType.RUM_SDK_CONFIG,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_rum_sdk_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMRemoteConfigApi(api_client)
    response = api_instance.update_rum_sdk_config(config_id="config_id", body=body)

    print(response)
