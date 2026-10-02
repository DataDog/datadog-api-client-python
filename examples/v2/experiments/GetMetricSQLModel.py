"""
Get metric SQL model returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    response = api_instance.get_metric_sql_model(
        metric_sql_model_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
    )

    print(response)
