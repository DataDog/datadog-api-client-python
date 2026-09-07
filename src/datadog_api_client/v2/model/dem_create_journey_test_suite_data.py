# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.dem_create_journey_test_suite_attributes import DemCreateJourneyTestSuiteAttributes
    from datadog_api_client.v2.model.dem_create_journey_test_suite_request_type import (
        DemCreateJourneyTestSuiteRequestType,
    )


class DemCreateJourneyTestSuiteData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.dem_create_journey_test_suite_attributes import (
            DemCreateJourneyTestSuiteAttributes,
        )
        from datadog_api_client.v2.model.dem_create_journey_test_suite_request_type import (
            DemCreateJourneyTestSuiteRequestType,
        )

        return {
            "attributes": (DemCreateJourneyTestSuiteAttributes,),
            "type": (DemCreateJourneyTestSuiteRequestType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        type: DemCreateJourneyTestSuiteRequestType,
        attributes: Union[DemCreateJourneyTestSuiteAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for a create test suite request.

        :param attributes: Attributes for creating a test suite for a DEM journey.
        :type attributes: DemCreateJourneyTestSuiteAttributes, optional

        :param type: The resource type for a request to create a DEM journey test suite.
        :type type: DemCreateJourneyTestSuiteRequestType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        super().__init__(kwargs)

        self_.type = type
