"""
Update archive order returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.logs_archive_order import LogsArchiveOrder
from datadog_api_client.v2.model.logs_archive_order_attributes import LogsArchiveOrderAttributes
from datadog_api_client.v2.model.logs_archive_order_definition import LogsArchiveOrderDefinition
from datadog_api_client.v2.model.logs_archive_order_definition_type import LogsArchiveOrderDefinitionType

body = LogsArchiveOrder(
    data=LogsArchiveOrderDefinition(
        attributes=LogsArchiveOrderAttributes(
            archive_ids=[
                "a2zcMylnM4OCHpYusxIi1g",
                "a2zcMylnM4OCHpYusxIi2g",
                "a2zcMylnM4OCHpYusxIi3g",
            ],
        ),
        type=LogsArchiveOrderDefinitionType.ARCHIVE_ORDER,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.update_logs_archive_order(body=body)

    print(response)
