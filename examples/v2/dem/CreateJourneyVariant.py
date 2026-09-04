"""
Create a DEM journey variant returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dem_api import DEMApi
from datadog_api_client.v2.model.dem_rum_node import DemRumNode
from datadog_api_client.v2.model.dem_rum_step import DemRumStep
from datadog_api_client.v2.model.dem_rum_step_type import DemRumStepType
from datadog_api_client.v2.model.dem_variant_attributes import DemVariantAttributes
from datadog_api_client.v2.model.dem_variant_request import DemVariantRequest
from datadog_api_client.v2.model.dem_variant_request_data import DemVariantRequestData
from datadog_api_client.v2.model.dem_variant_type import DemVariantType

body = DemVariantRequest(
    data=DemVariantRequestData(
        attributes=DemVariantAttributes(
            filter="device.type:mobile",
            name="Mobile checkout",
            rum_steps=[
                DemRumStep(
                    nodes=[
                        DemRumNode(
                            query="action.name:'checkout'",
                        ),
                    ],
                    type=DemRumStepType.START,
                ),
                DemRumStep(
                    nodes=[
                        DemRumNode(
                            query="action.name:'confirmation'",
                        ),
                    ],
                    type=DemRumStepType.STOP,
                ),
            ],
        ),
        type=DemVariantType.VARIANTS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DEMApi(api_client)
    response = api_instance.create_journey_variant(journey_id="journey_id", body=body)

    print(response)
