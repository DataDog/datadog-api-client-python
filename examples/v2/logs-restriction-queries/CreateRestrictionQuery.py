"""
Create a restriction query returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.logs_restriction_queries_api import LogsRestrictionQueriesApi
from datadog_api_client.v2.model.logs_restriction_queries_type import LogsRestrictionQueriesType
from datadog_api_client.v2.model.restriction_query_create_attributes import RestrictionQueryCreateAttributes
from datadog_api_client.v2.model.restriction_query_create_data import RestrictionQueryCreateData
from datadog_api_client.v2.model.restriction_query_create_payload import RestrictionQueryCreatePayload

body = RestrictionQueryCreatePayload(
    data=RestrictionQueryCreateData(
        attributes=RestrictionQueryCreateAttributes(
            restriction_query="env:sandbox",
        ),
        type=LogsRestrictionQueriesType.LOGS_RESTRICTION_QUERIES,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_restriction_query"] = True
with ApiClient(configuration) as api_client:
    api_instance = LogsRestrictionQueriesApi(api_client)
    response = api_instance.create_restriction_query(body=body)

    print(response)
