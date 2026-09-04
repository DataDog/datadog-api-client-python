"""
Update a DEM journey returns "OK" response
"""

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.dem_api import DEMApi
from datadog_api_client.v2.model.dem_journey_create_attributes import DemJourneyCreateAttributes
from datadog_api_client.v2.model.dem_journey_create_data import DemJourneyCreateData
from datadog_api_client.v2.model.dem_journey_create_request import DemJourneyCreateRequest
from datadog_api_client.v2.model.dem_journey_rum import DemJourneyRum
from datadog_api_client.v2.model.dem_journey_type import DemJourneyType
from datadog_api_client.v2.model.dem_rum_node import DemRumNode
from datadog_api_client.v2.model.dem_rum_step import DemRumStep
from datadog_api_client.v2.model.dem_rum_step_type import DemRumStepType
from datadog_api_client.v2.model.dem_variant import DemVariant

body = DemJourneyCreateRequest(
    data=DemJourneyCreateData(
        attributes=DemJourneyCreateAttributes(
            description="Tracks the user checkout flow from cart to confirmation.",
            journey_rum=DemJourneyRum(
                filter="env:prod",
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
                variants=[
                    DemVariant(
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
                ],
            ),
            name="Checkout Flow",
            tags=[
                "team:synthetics",
                "env:prod",
            ],
            variants=[
                DemVariant(
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
            ],
        ),
        type=DemJourneyType.JOURNEYS,
    ),
)

configuration = Configuration()
with ApiClient(configuration) as api_client:
    api_instance = DEMApi(api_client)
    response = api_instance.update_journey(journey_id="journey_id", body=body)

    print(response)
