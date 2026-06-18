"""
Update Vercel configuration returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.vercel_api import VercelApi
from datadog_api_client.v2.model.vercel_api_key import VercelApiKey
from datadog_api_client.v2.model.vercel_config_attributes import VercelConfigAttributes
from datadog_api_client.v2.model.vercel_environment import VercelEnvironment
from datadog_api_client.v2.model.vercel_log_source import VercelLogSource
from datadog_api_client.v2.model.vercel_logs_config import VercelLogsConfig
from datadog_api_client.v2.model.vercel_trace_config import VercelTraceConfig

body = VercelConfigAttributes(
    api_key=VercelApiKey(
        id="00000000-0000-0000-0000-000000000001",
        value="",
    ),
    logs_config=VercelLogsConfig(
        enabled=True,
        environments=[
            VercelEnvironment.PRODUCTION,
        ],
        log_sources=[
            VercelLogSource.LAMBDA,
        ],
        sampling_percentage=100,
    ),
    trace_config=VercelTraceConfig(
        enabled=True,
        is_deprecated_otel=False,
        sampling_percentage=100,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = VercelApi(api_client)
    api_instance.update_vercel_config(configuration_id="configuration_id", body=body)
