"""
Get rows by id returns "Some or all requested rows were found." response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.reference_tables_api import ReferenceTablesApi

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = ReferenceTablesApi(api_client)
    response = api_instance.get_rows_by_id(
        id="id",
        row_id=[],
    )

    print(response)
