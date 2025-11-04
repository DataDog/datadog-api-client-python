"""
Get account facet info returns "Successful response with facet information" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.rum_audience_management_api import RumAudienceManagementApi
from datadog_api_client.v2.model.facet_info_request import FacetInfoRequest
from datadog_api_client.v2.model.facet_info_request_data import FacetInfoRequestData
from datadog_api_client.v2.model.facet_info_request_data_attributes import FacetInfoRequestDataAttributes
from datadog_api_client.v2.model.facet_info_request_data_attributes_search import FacetInfoRequestDataAttributesSearch
from datadog_api_client.v2.model.facet_info_request_data_attributes_term_search import (
    FacetInfoRequestDataAttributesTermSearch,
)
from datadog_api_client.v2.model.facet_info_request_data_type import FacetInfoRequestDataType

body = FacetInfoRequest(
    data=FacetInfoRequestData(
        attributes=FacetInfoRequestDataAttributes(
            facet_id="first_browser_name",
            limit=10,
            search=FacetInfoRequestDataAttributesSearch(
                query="user_org_id:5001 AND first_country_code:US",
            ),
            term_search=FacetInfoRequestDataAttributesTermSearch(
                value="Chrome",
            ),
        ),
        id="facet_info_request",
        type=FacetInfoRequestDataType.USERS_FACET_INFO_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_account_facet_info"] = True
with ApiClient(configuration) as api_client:
    api_instance = RumAudienceManagementApi(api_client)
    response = api_instance.get_account_facet_info(body=body)

    print(response)
