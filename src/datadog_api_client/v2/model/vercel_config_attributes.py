# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.vercel_api_key import VercelApiKey
    from datadog_api_client.v2.model.vercel_logs_config import VercelLogsConfig
    from datadog_api_client.v2.model.vercel_trace_config import VercelTraceConfig


class VercelConfigAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.vercel_api_key import VercelApiKey
        from datadog_api_client.v2.model.vercel_logs_config import VercelLogsConfig
        from datadog_api_client.v2.model.vercel_trace_config import VercelTraceConfig

        return {
            "api_key": (VercelApiKey,),
            "logs_config": (VercelLogsConfig,),
            "trace_config": (VercelTraceConfig,),
        }

    attribute_map = {
        "api_key": "apiKey",
        "logs_config": "logsConfig",
        "trace_config": "traceConfig",
    }

    def __init__(
        self_, api_key: VercelApiKey, logs_config: VercelLogsConfig, trace_config: VercelTraceConfig, **kwargs
    ):
        """
        Attributes of the Datadog Vercel integration configuration.

        :param api_key: Datadog API key reference used by the Vercel integration to send telemetry.
        :type api_key: VercelApiKey

        :param logs_config: Logs forwarding configuration for the Vercel integration.
        :type logs_config: VercelLogsConfig

        :param trace_config: Tracing configuration for the Vercel integration.
        :type trace_config: VercelTraceConfig
        """
        super().__init__(kwargs)

        self_.api_key = api_key
        self_.logs_config = logs_config
        self_.trace_config = trace_config
