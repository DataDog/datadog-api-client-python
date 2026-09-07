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
    from datadog_api_client.v2.model.dem_journey_create_data import DemJourneyCreateData


class DemJourneyCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_journey_create_data import DemJourneyCreateData

        return {
            "data": (DemJourneyCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: DemJourneyCreateData, **kwargs):
        """
        Request body for creating or updating a DEM journey.

        :param data: Data object for a DEM journey create or update request.
        :type data: DemJourneyCreateData
        """
        super().__init__(kwargs)

        self_.data = data
