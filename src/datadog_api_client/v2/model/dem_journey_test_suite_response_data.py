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
    from datadog_api_client.v2.model.dem_journey_test_suite_response_attributes import (
        DemJourneyTestSuiteResponseAttributes,
    )
    from datadog_api_client.v2.model.dem_journey_test_suite_type import DemJourneyTestSuiteType


class DemJourneyTestSuiteResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_journey_test_suite_response_attributes import (
            DemJourneyTestSuiteResponseAttributes,
        )
        from datadog_api_client.v2.model.dem_journey_test_suite_type import DemJourneyTestSuiteType

        return {
            "attributes": (DemJourneyTestSuiteResponseAttributes,),
            "id": (str,),
            "type": (DemJourneyTestSuiteType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: DemJourneyTestSuiteResponseAttributes, id: str, type: DemJourneyTestSuiteType, **kwargs
    ):
        """
        Data object in a DEM test suite response.

        :param attributes: Attributes of a DEM journey test suite response.
        :type attributes: DemJourneyTestSuiteResponseAttributes

        :param id: The public ID of the test suite.
        :type id: str

        :param type: The type identifier for DEM journey test suites.
        :type type: DemJourneyTestSuiteType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
