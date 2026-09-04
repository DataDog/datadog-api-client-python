# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dem_journey_create_attributes import DemJourneyCreateAttributes
    from datadog_api_client.v2.model.dem_journey_type import DemJourneyType


class DemJourneyCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_journey_create_attributes import DemJourneyCreateAttributes
        from datadog_api_client.v2.model.dem_journey_type import DemJourneyType

        return {
            "attributes": (DemJourneyCreateAttributes,),
            "type": (DemJourneyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: DemJourneyCreateAttributes, type: DemJourneyType, **kwargs):
        """
        Data object for a DEM journey create or update request.

        :param attributes: Attributes for creating or updating a DEM journey.
        :type attributes: DemJourneyCreateAttributes

        :param type: The type identifier for DEM journeys.
        :type type: DemJourneyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
