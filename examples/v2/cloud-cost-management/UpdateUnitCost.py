"""
Update a unit cost returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.cloud_cost_management_api import CloudCostManagementApi
from datadog_api_client.v2.model.unit_cost_formula import UnitCostFormula
from datadog_api_client.v2.model.unit_cost_query import UnitCostQuery
from datadog_api_client.v2.model.unit_cost_query_definition import UnitCostQueryDefinition
from datadog_api_client.v2.model.unit_cost_request_attributes import UnitCostRequestAttributes
from datadog_api_client.v2.model.unit_cost_type import UnitCostType
from datadog_api_client.v2.model.unit_cost_update_request import UnitCostUpdateRequest
from datadog_api_client.v2.model.unit_cost_update_request_data import UnitCostUpdateRequestData
from uuid import UUID

body = UnitCostUpdateRequest(
    data=UnitCostUpdateRequestData(
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
        id=UUID("64aecd58-e355-4f07-9c3a-56ff6bda6cd8"),
        type=UnitCostType.UNIT_COST,
    ),
)

configuration = Configuration()
configuration.unstable_operations["update_unit_cost"] = True
with ApiClient(configuration) as api_client:
    api_instance = CloudCostManagementApi(api_client)
    response = api_instance.update_unit_cost(unit_cost_id=UUID("9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d"), body=body)

    print(response)
