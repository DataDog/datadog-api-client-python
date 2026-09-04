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
    from datadog_api_client.v2.model.dem_journey_response_attributes import DemJourneyResponseAttributes
    from datadog_api_client.v2.model.dem_journey_type import DemJourneyType


class DemJourneyResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_journey_response_attributes import DemJourneyResponseAttributes
        from datadog_api_client.v2.model.dem_journey_type import DemJourneyType

        return {
            "attributes": (DemJourneyResponseAttributes,),
            "id": (str,),
            "type": (DemJourneyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DemJourneyResponseAttributes, id: str, type: DemJourneyType, **kwargs):
        """
        Data object in a DEM journey response.

        :param attributes: Attributes returned in a DEM journey response.
        :type attributes: DemJourneyResponseAttributes

        :param id: The unique identifier of the DEM journey.
        :type id: str

        :param type: The type identifier for DEM journeys.
        :type type: DemJourneyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
