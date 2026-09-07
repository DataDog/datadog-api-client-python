# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DemJourneyTestSuiteType(ModelSimple):
    """
    The type identifier for DEM journey test suites.

    :param value: If omitted defaults to "journey_test_suite". Must be one of ["journey_test_suite"].
    :type value: str
    """

    allowed_values = {
        "journey_test_suite",
    }
    JOURNEY_TEST_SUITE: ClassVar["DemJourneyTestSuiteType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DemJourneyTestSuiteType.JOURNEY_TEST_SUITE = DemJourneyTestSuiteType("journey_test_suite")
