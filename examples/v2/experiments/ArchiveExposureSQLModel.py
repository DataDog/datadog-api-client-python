"""
Archive exposure SQL model returns "The exposure SQL model was archived. Archiving an already-archived model succeeds
and leaves the original archive time in place." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    api_instance.archive_exposure_sql_model(
        exposure_sql_model_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
    )
