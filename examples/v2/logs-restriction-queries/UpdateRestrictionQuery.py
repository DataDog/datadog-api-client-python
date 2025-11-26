"""
Update a restriction query returns "OK" response
"""

from os import environ
from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType
from datadog_api_client.v2.model.restriction_query_update_attributes import RestrictionQueryUpdateAttributes
from datadog_api_client.v2.model.restriction_query_update_data import RestrictionQueryUpdateData
from datadog_api_client.v2.model.restriction_query_update_payload import RestrictionQueryUpdatePayload

# there is a valid "restriction_query" in the system
RESTRICTION_QUERY_DATA_ID = environ["RESTRICTION_QUERY_DATA_ID"]

body = RestrictionQueryUpdatePayload(
    data=RestrictionQueryUpdateData(
        attributes=RestrictionQueryUpdateAttributes(
            restriction_query="env:production",
        ),
        type=LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.update_restriction_query(restriction_query_id=RESTRICTION_QUERY_DATA_ID, body=body)

    print(response)
