# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DemCreateJourneyTestSuiteRequestType(ModelSimple):
    """
    The resource type for a request to create a DEM journey test suite.

    :param value: If omitted defaults to "create_test_suite_for_journey_request". Must be one of ["create_test_suite_for_journey_request"].
    :type value: str
    """

    allowed_values = {
        "create_test_suite_for_journey_request",
    }
    CREATE_TEST_SUITE_FOR_JOURNEY_REQUEST: ClassVar["DemCreateJourneyTestSuiteRequestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DemCreateJourneyTestSuiteRequestType.CREATE_TEST_SUITE_FOR_JOURNEY_REQUEST = DemCreateJourneyTestSuiteRequestType(
    "create_test_suite_for_journey_request"
)
