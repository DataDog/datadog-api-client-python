"""
Create a unit cost returns "Created" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.unit_cost_create_request import UnitCostCreateRequest
from datadog_api_client.v2.model.unit_cost_create_request_data import UnitCostCreateRequestData
from datadog_api_client.v2.model.unit_cost_formula import UnitCostFormula
from datadog_api_client.v2.model.unit_cost_query import UnitCostQuery
from datadog_api_client.v2.model.unit_cost_query_definition import UnitCostQueryDefinition
from datadog_api_client.v2.model.unit_cost_request_attributes import UnitCostRequestAttributes
from datadog_api_client.v2.model.unit_cost_type import UnitCostType

body = UnitCostCreateRequest(
    data=UnitCostCreateRequestData(
        attributes=UnitCostRequestAttributes(
            denominator_query=UnitCostQueryDefinition(
                formulas=[
                    UnitCostFormula([("formula", "numerator")]),
                ],
                queries=[
                    UnitCostQuery(
                        [
                            ("data_source", "cloud_cost"),
                            ("name", "numerator"),
                            ("query", "sum:aws.cost.net.amortized.shared.resources.allocated{*}.rollup(sum, daily)"),
                        ]
                    ),
                ],
            ),
            description="Amortized cloud spend divided by the number of active users.",
            name="Cloud cost per active user",
            numerator_query=UnitCostQueryDefinition(
                formulas=[
                    UnitCostFormula([("formula", "numerator")]),
                ],
                queries=[
                    UnitCostQuery(
                        [
                            ("data_source", "cloud_cost"),
                            ("name", "numerator"),
                            ("query", "sum:aws.cost.net.amortized.shared.resources.allocated{*}.rollup(sum, daily)"),
                        ]
                    ),
                ],
            ),
            unit_label="user",
        ),
        type=UnitCostType.UNIT_COST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["create_unit_cost"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.create_unit_cost(body=body)

    print(response)
