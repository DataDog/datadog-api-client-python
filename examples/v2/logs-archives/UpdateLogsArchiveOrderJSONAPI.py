"""
Update archive order returns "OK" response using JSON:API models
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_archives_api import LogsArchivesApi
from datadog_api_client.v2.model.logs_archive_order import LogsArchiveOrderJSON

body = LogsArchiveOrderJSON(
    archive_ids=[
        "a2zcMylnM4OCHpYusxIi1g",
        "a2zcMylnM4OCHpYusxIi2g",
        "a2zcMylnM4OCHpYusxIi3g",
    ],
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = LogsArchivesApi(api_client)
    response = api_instance.update_logs_archive_order(body=body)

    print(response)
