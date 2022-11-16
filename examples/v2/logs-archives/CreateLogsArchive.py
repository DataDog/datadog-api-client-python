"""
Create an archive returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.logs_archive_create_request import LogsArchiveCreateRequest
from datadog_api_client.v2.model.logs_archive_create_request_attributes import LogsArchiveCreateRequestAttributes
from datadog_api_client.v2.model.logs_archive_create_request_definition import LogsArchiveCreateRequestDefinition
from datadog_api_client.v2.model.logs_archive_destination_azure import LogsArchiveDestinationAzure
from datadog_api_client.v2.model.logs_archive_destination_azure_type import LogsArchiveDestinationAzureType
from datadog_api_client.v2.model.logs_archive_integration_azure import LogsArchiveIntegrationAzure

body = LogsArchiveCreateRequest(
    data=LogsArchiveCreateRequestDefinition(
        attributes=LogsArchiveCreateRequestAttributes(
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
        ),
        type="archives",
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.create_logs_archive(body=body)

    print(response)
