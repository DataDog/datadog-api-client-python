# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dem_inferred_journey_item import DemInferredJourneyItem
    from datadog_api_client.v2.model.dem_inferred_journey_candidate_data import DemInferredJourneyCandidateData
    from datadog_api_client.v2.model.dem_inferred_journey_ignored_data import DemInferredJourneyIgnoredData


class DemSearchInferredJourneysResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_inferred_journey_item import DemInferredJourneyItem

        return {
            "data": ([DemInferredJourneyItem],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(
        self_,
        data: List[Union[DemInferredJourneyItem, DemInferredJourneyCandidateData, DemInferredJourneyIgnoredData]],
        **kwargs,
    ):
        """
        Response body for searching inferred journeys. Contains either candidate or ignored items depending on the ``status`` query parameter.

        :param data: List of inferred journey items matching the search criteria.
        :type data: [DemInferredJourneyItem]
        """
        super().__init__(kwargs)

        self_.data = data
