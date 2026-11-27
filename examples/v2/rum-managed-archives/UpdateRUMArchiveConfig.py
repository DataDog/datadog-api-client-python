"""
Create or update an archive configuration returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_managed_archives_api import RUMManagedArchivesApi
from datadog_api_client.v2.model.rum_archive_config_type import RumArchiveConfigType
from datadog_api_client.v2.model.rum_archive_config_upsert_attributes import RumArchiveConfigUpsertAttributes
from datadog_api_client.v2.model.rum_archive_config_upsert_data import RumArchiveConfigUpsertData
from datadog_api_client.v2.model.rum_archive_config_upsert_request import RumArchiveConfigUpsertRequest

# there is a valid "rum_application" in the system
RUM_APPLICATION_DATA_ID = environ["RUM_APPLICATION_DATA_ID"]

body = RumArchiveConfigUpsertRequest(
    data=RumArchiveConfigUpsertData(
        attributes=RumArchiveConfigUpsertAttributes(
            enabled=True,
            retention_days=90,
        ),
        id=RUM_APPLICATION_DATA_ID,
        type=RumArchiveConfigType.RUM_ARCHIVE_CONFIG,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = RUMManagedArchivesApi(api_client)
    response = api_instance.update_rum_archive_config(app_id=RUM_APPLICATION_DATA_ID, body=body)

    print(response)
