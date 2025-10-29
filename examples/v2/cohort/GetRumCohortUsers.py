"""
Get rum cohort users returns "Successful response with cohort users" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cohort_api import CohortApi
from datadog_api_client.v2.model.get_cohort_users_request import GetCohortUsersRequest
from datadog_api_client.v2.model.get_cohort_users_request_data import GetCohortUsersRequestData
from datadog_api_client.v2.model.get_cohort_users_request_data_attributes import GetCohortUsersRequestDataAttributes
from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition import (
    GetCohortUsersRequestDataAttributesDefinition,
)
from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters import (
    GetCohortUsersRequestDataAttributesDefinitionAudienceFilters,
)
from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_accounts_items import (
    GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersAccountsItems,
)
from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_segments_items import (
    GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersSegmentsItems,
)
from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_definition_audience_filters_users_items import (
    GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersUsersItems,
)
from datadog_api_client.v2.model.get_cohort_users_request_data_attributes_time import (
    GetCohortUsersRequestDataAttributesTime,
)
from datadog_api_client.v2.model.get_cohort_users_request_data_type import GetCohortUsersRequestDataType

body = GetCohortUsersRequest(
    data=GetCohortUsersRequestData(
        attributes=GetCohortUsersRequestDataAttributes(
            definition=GetCohortUsersRequestDataAttributesDefinition(
                audience_filters=GetCohortUsersRequestDataAttributesDefinitionAudienceFilters(
                    accounts=[
                        GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersAccountsItems(
                            name="",
                        ),
                    ],
                    segments=[
                        GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersSegmentsItems(
                            name="",
                            segment_id="",
                        ),
                    ],
                    users=[
                        GetCohortUsersRequestDataAttributesDefinitionAudienceFiltersUsersItems(
                            name="",
                        ),
                    ],
                ),
            ),
            time=GetCohortUsersRequestDataAttributesTime(),
        ),
        type=GetCohortUsersRequestDataType.COHORT_USERS_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_rum_cohort_users"] = True
with ApiClient(configuration) as api_client:
    api_instance = CohortApi(api_client)
    response = api_instance.get_rum_cohort_users(body=body)

    print(response)
