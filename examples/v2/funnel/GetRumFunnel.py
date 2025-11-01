"""
Get rum funnel returns "Successful response with funnel analysis data" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.funnel_api import FunnelApi
from datadog_api_client.v2.model.funnel_request import FunnelRequest
from datadog_api_client.v2.model.funnel_request_data import FunnelRequestData
from datadog_api_client.v2.model.funnel_request_data_attributes import FunnelRequestDataAttributes
from datadog_api_client.v2.model.funnel_request_data_attributes_search import FunnelRequestDataAttributesSearch
from datadog_api_client.v2.model.funnel_request_data_attributes_search_steps_items import (
    FunnelRequestDataAttributesSearchStepsItems,
)
from datadog_api_client.v2.model.funnel_request_data_attributes_time import FunnelRequestDataAttributesTime
from datadog_api_client.v2.model.funnel_request_data_type import FunnelRequestDataType

body = FunnelRequest(
    data=FunnelRequestData(
        attributes=FunnelRequestDataAttributes(
            data_source="rum",
            enforced_execution_type="",
            request_id="",
            search=FunnelRequestDataAttributesSearch(
                cross_session_filter="",
                query_string="@type:view",
                steps=[
                    FunnelRequestDataAttributesSearchStepsItems(
                        facet="@view.name",
                        step_filter="",
                        value="/apm/home",
                    ),
                    FunnelRequestDataAttributesSearchStepsItems(
                        facet="@view.name",
                        step_filter="",
                        value="/apm/traces",
                    ),
                ],
                subquery_id="",
            ),
            time=FunnelRequestDataAttributesTime(
                _from=1756425600000,
                to=1756857600000,
            ),
        ),
        id="funnel_request",
        type=FunnelRequestDataType.FUNNEL_REQUEST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["get_rum_funnel"] = True
with ApiClient(configuration) as api_client:
    api_instance = FunnelApi(api_client)
    response = api_instance.get_rum_funnel(body=body)

    print(response)
