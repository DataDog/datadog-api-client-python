"""
Update an archive returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.logs_archive_create_request import LogsArchiveCreateRequestJSON
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
from datadog_api_client.v2.model.logs_archive_destination_azure_type import LogsArchiveDestinationAzureType
from datadog_api_client.v2.model.logs_archive_integration_azure import LogsArchiveIntegrationAzure

body = LogsArchiveCreateRequestJSON(
    destination=LogsArchiveDestinationAzure(
        container="container-name",
        integration=LogsArchiveIntegrationAzure(
            client_id="aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
            tenant_id="aaaaaaaa-1a1a-1a1a-1a1a-aaaaaaaaaaaa",
        ),
        storage_account="account-name",
        type=LogsArchiveDestinationAzureType.AZURE,
    ),
    include_tags=False,
    name="Nginx Archive",
    query="source:nginx",
    rehydration_max_scan_size_in_gb=100,
    rehydration_tags=[
        "team:intake",
        "team:app",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.update_logs_archive(archive_id="archive_id", body=body)

    print(response)
