"""
Set default subject type returns "The subject type is now the organization's default." response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.experiments_api import ExperimentsApi
from uuid import UUID

configuration = Configuration()
configuration.access_token = environ["DD_BEARER_TOKEN"]
with ApiClient(configuration) as api_client:
    api_instance = ExperimentsApi(api_client)
    api_instance.set_default_subject_type(
        subject_type_id=UUID("550e8400-e29b-41d4-a716-446655440000"),
    )
