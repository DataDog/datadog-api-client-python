"""
Get rum sankey returns "Successful response with Sankey diagram data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.user_flow_api import UserFlowApi
from datadog_api_client.v2.model.sankey_request import SankeyRequest
from datadog_api_client.v2.model.sankey_request_data import SankeyRequestData
from datadog_api_client.v2.model.sankey_request_data_attributes import SankeyRequestDataAttributes
from datadog_api_client.v2.model.sankey_request_data_attributes_definition import SankeyRequestDataAttributesDefinition
from datadog_api_client.v2.model.sankey_request_data_attributes_sampling import SankeyRequestDataAttributesSampling
from datadog_api_client.v2.model.sankey_request_data_attributes_search import SankeyRequestDataAttributesSearch
from datadog_api_client.v2.model.sankey_request_data_attributes_search_audience_filters import (
    SankeyRequestDataAttributesSearchAudienceFilters,
)
from datadog_api_client.v2.model.sankey_request_data_attributes_time import SankeyRequestDataAttributesTime
from datadog_api_client.v2.model.sankey_request_data_type import SankeyRequestDataType

body = SankeyRequest(
    data=SankeyRequestData(
        attributes=SankeyRequestDataAttributes(
            data_source="",
            definition=SankeyRequestDataAttributesDefinition(
                entries_per_step=10,
                number_of_steps=5,
                source="@view.name",
                target="@view.name",
            ),
            enforced_execution_type="",
            request_id="",
            sampling=SankeyRequestDataAttributesSampling(
                enabled=True,
            ),
            search=SankeyRequestDataAttributesSearch(
                audience_filters=SankeyRequestDataAttributesSearchAudienceFilters(),
                query="@type:view @application.id:*",
                subquery_id="",
            ),
            time=SankeyRequestDataAttributesTime(
                _from=1756425600000,
                to=1756857600000,
            ),
        ),
        id="sankey_request",
        type=SankeyRequestDataType.SANKEY_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_rum_sankey"] = True
with ApiClient(configuration) as api_client:
    api_instance = UserFlowApi(api_client)
    response = api_instance.get_rum_sankey(body=body)

    print(response)
