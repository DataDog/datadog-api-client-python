"""
Update a RUM SDK configuration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_remote_config_api import RUMRemoteConfigApi
from datadog_api_client.v2.model.rum_sdk_config_dynamic_option import RUMSdkConfigDynamicOption
from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_pair import RUMSdkConfigDynamicOptionPair
from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_serialized_type import (
    RUMSdkConfigDynamicOptionSerializedType,
)
from datadog_api_client.v2.model.rum_sdk_config_dynamic_option_strategy import RUMSdkConfigDynamicOptionStrategy
from datadog_api_client.v2.model.rum_sdk_config_match_option import RUMSdkConfigMatchOption
from datadog_api_client.v2.model.rum_sdk_config_match_option_serialized_type import (
    RUMSdkConfigMatchOptionSerializedType,
)
from datadog_api_client.v2.model.rum_sdk_config_rum_update_attributes import RUMSdkConfigRUMUpdateAttributes
from datadog_api_client.v2.model.rum_sdk_config_serialized_regex import RUMSdkConfigSerializedRegex
from datadog_api_client.v2.model.rum_sdk_config_serialized_regex_type import RUMSdkConfigSerializedRegexType
from datadog_api_client.v2.model.rum_sdk_config_tracing_url_config import RUMSdkConfigTracingUrlConfig
from datadog_api_client.v2.model.rum_sdk_config_tracing_url_propagator_type import RUMSdkConfigTracingUrlPropagatorType
from datadog_api_client.v2.model.rum_sdk_config_type import RUMSdkConfigType
from datadog_api_client.v2.model.rum_sdk_config_update_attributes import RUMSdkConfigUpdateAttributes
from datadog_api_client.v2.model.rum_sdk_config_update_data import RUMSdkConfigUpdateData
from datadog_api_client.v2.model.rum_sdk_config_update_request import RUMSdkConfigUpdateRequest

body = RUMSdkConfigUpdateRequest(
    data=RUMSdkConfigUpdateData(
        attributes=RUMSdkConfigUpdateAttributes(
            rum=RUMSdkConfigRUMUpdateAttributes(
                allowed_tracing_urls=[
                    RUMSdkConfigTracingUrlConfig(
                        match=RUMSdkConfigMatchOption(
                            rc_serialized_type=RUMSdkConfigMatchOptionSerializedType.STRING,
                            value="https://app.datadoghq.com",
                        ),
                        propagator_types=[
                            RUMSdkConfigTracingUrlPropagatorType.DATADOG,
                            RUMSdkConfigTracingUrlPropagatorType.TRACECONTEXT,
                        ],
                    ),
                ],
                allowed_tracking_origins=[
                    RUMSdkConfigMatchOption(
                        rc_serialized_type=RUMSdkConfigMatchOptionSerializedType.STRING,
                        value="https://app.datadoghq.com",
                    ),
                ],
                context=[
                    RUMSdkConfigDynamicOptionPair(
                        key="id",
                        value=RUMSdkConfigDynamicOption(
                            attribute="data-version",
                            extractor=RUMSdkConfigSerializedRegex(
                                rc_serialized_type=RUMSdkConfigSerializedRegexType.REGEX,
                                value="^https://app-.*.datadoghq.com",
                            ),
                            key="app.version",
                            name="app_version",
                            path="application.version",
                            rc_serialized_type=RUMSdkConfigDynamicOptionSerializedType.DYNAMIC,
                            selector="#app-version",
                            strategy=RUMSdkConfigDynamicOptionStrategy.JS,
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
                    RUMSdkConfigDynamicOptionPair(
                        key="id",
                        value=RUMSdkConfigDynamicOption(
                            attribute="data-version",
                            extractor=RUMSdkConfigSerializedRegex(
                                rc_serialized_type=RUMSdkConfigSerializedRegexType.REGEX,
                                value="^https://app-.*.datadoghq.com",
                            ),
                            key="app.version",
                            name="app_version",
                            path="application.version",
                            rc_serialized_type=RUMSdkConfigDynamicOptionSerializedType.DYNAMIC,
                            selector="#app-version",
                            strategy=RUMSdkConfigDynamicOptionStrategy.JS,
                        ),
                    ),
                ],
                version=RUMSdkConfigDynamicOption(
                    attribute="data-version",
                    extractor=RUMSdkConfigSerializedRegex(
                        rc_serialized_type=RUMSdkConfigSerializedRegexType.REGEX,
                        value="^https://app-.*.datadoghq.com",
                    ),
                    key="app.version",
                    name="app_version",
                    path="application.version",
                    rc_serialized_type=RUMSdkConfigDynamicOptionSerializedType.DYNAMIC,
                    selector="#app-version",
                    strategy=RUMSdkConfigDynamicOptionStrategy.JS,
                ),
            ),
        ),
        id="abc12345-1234-5678-abcd-ef1234567890",
        type=RUMSdkConfigType.RUM_SDK_CONFIG,
    ),
)

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["update_rum_sdk_config"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMRemoteConfigApi(api_client)
    response = api_instance.update_rum_sdk_config(config_id="config_id", body=body)

    print(response)
