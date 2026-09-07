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
    from datadog_api_client.v2.model.dem_recommended_test_attributes import DemRecommendedTestAttributes
    from datadog_api_client.v2.model.dem_recommended_test_type import DemRecommendedTestType


class DemRecommendedTestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_recommended_test_attributes import DemRecommendedTestAttributes
        from datadog_api_client.v2.model.dem_recommended_test_type import DemRecommendedTestType

        return {
            "attributes": (DemRecommendedTestAttributes,),
            "id": (str,),
            "type": (DemRecommendedTestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: DemRecommendedTestAttributes, id: str, type: DemRecommendedTestType, **kwargs):
        """
        Data object for a recommended synthetic test.

        :param attributes: Attributes of an AI-recommended synthetic test for a DEM journey.
        :type attributes: DemRecommendedTestAttributes

        :param id: The identifier of the journey associated with the recommendation.
        :type id: str

        :param type: The type identifier for a recommended synthetic test.
        :type type: DemRecommendedTestType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
