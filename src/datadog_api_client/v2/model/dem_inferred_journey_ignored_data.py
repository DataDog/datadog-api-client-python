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
    from datadog_api_client.v2.model.dem_inferred_journey_ignored_attributes import DemInferredJourneyIgnoredAttributes
    from datadog_api_client.v2.model.dem_journey_type import DemJourneyType


class DemInferredJourneyIgnoredData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_inferred_journey_ignored_attributes import (
            DemInferredJourneyIgnoredAttributes,
        )
        from datadog_api_client.v2.model.dem_journey_type import DemJourneyType

        return {
            "attributes": (DemInferredJourneyIgnoredAttributes,),
            "id": (str,),
            "type": (DemJourneyType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DemInferredJourneyIgnoredAttributes, id: str, type: DemJourneyType, **kwargs):
        """
        Data object for an ignored inferred journey.

        :param attributes: Attributes of an ignored inferred journey.
        :type attributes: DemInferredJourneyIgnoredAttributes

        :param id: The unique identifier of the ignored inferred journey.
        :type id: str

        :param type: The type identifier for DEM journeys.
        :type type: DemJourneyType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
