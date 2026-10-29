"""
Restore source maps returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_api import RUMApi
from datadog_api_client.v2.model.sourcemap_map_kind import SourcemapMapKind
from datadog_api_client.v2.model.sourcemap_symbol_type import SourcemapSymbolType

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
configuration.unstable_operations["restore_sourcemaps"] = True
with ApiClient(configuration) as api_client:
    api_instance = RUMApi(api_client)
    response = api_instance.restore_sourcemaps(
        mapkind=SourcemapMapKind.WASM,
        symbol_type=SourcemapSymbolType.SOURCEMAP,
        dry_run=True,
        filter_service=[
            "nonexistent-svc",
        ],
        filter_version=[
            "0.0.0-none",
        ],
    )

    print(response)
