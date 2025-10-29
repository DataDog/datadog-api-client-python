"""
Get rum cohort returns "Successful response with cohort analysis data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cohort_api import CohortApi
from datadog_api_client.v2.model.get_cohort_request import GetCohortRequest
from datadog_api_client.v2.model.get_cohort_request_data import GetCohortRequestData
from datadog_api_client.v2.model.get_cohort_request_data_attributes import GetCohortRequestDataAttributes
from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition import (
    GetCohortRequestDataAttributesDefinition,
)
from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition_audience_filters import (
    GetCohortRequestDataAttributesDefinitionAudienceFilters,
)
from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition_audience_filters_accounts_items import (
    GetCohortRequestDataAttributesDefinitionAudienceFiltersAccountsItems,
)
from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition_audience_filters_segments_items import (
    GetCohortRequestDataAttributesDefinitionAudienceFiltersSegmentsItems,
)
from datadog_api_client.v2.model.get_cohort_request_data_attributes_definition_audience_filters_users_items import (
    GetCohortRequestDataAttributesDefinitionAudienceFiltersUsersItems,
)
from datadog_api_client.v2.model.get_cohort_request_data_attributes_time import GetCohortRequestDataAttributesTime
from datadog_api_client.v2.model.get_cohort_request_data_type import GetCohortRequestDataType

body = GetCohortRequest(
    data=GetCohortRequestData(
        attributes=GetCohortRequestDataAttributes(
            definition=GetCohortRequestDataAttributesDefinition(
                audience_filters=GetCohortRequestDataAttributesDefinitionAudienceFilters(
                    accounts=[
                        GetCohortRequestDataAttributesDefinitionAudienceFiltersAccountsItems(
                            name="",
                        ),
                    ],
                    segments=[
                        GetCohortRequestDataAttributesDefinitionAudienceFiltersSegmentsItems(
                            name="",
                            segment_id="",
                        ),
                    ],
                    users=[
                        GetCohortRequestDataAttributesDefinitionAudienceFiltersUsersItems(
                            name="",
                        ),
                    ],
                ),
            ),
            time=GetCohortRequestDataAttributesTime(),
        ),
        type=GetCohortRequestDataType.COHORT_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_rum_cohort"] = True
with ApiClient(configuration) as api_client:
    api_instance = CohortApi(api_client)
    response = api_instance.get_rum_cohort(body=body)

    print(response)
