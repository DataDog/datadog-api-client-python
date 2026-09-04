# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class DemCreateJourneyTestSuiteAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "include_tests_from_journey_coverage": (bool, none_type),
            "test_suite_name": (str, none_type),
        }

    attribute_map = {
        "include_tests_from_journey_coverage": "include_tests_from_journey_coverage",
        "test_suite_name": "test_suite_name",
    }

    def __init__(
        self_,
        include_tests_from_journey_coverage: Union[bool, none_type, UnsetType] = unset,
        test_suite_name: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a test suite for a DEM journey.

        :param include_tests_from_journey_coverage: Whether to populate the test suite based on journey coverage data.
        :type include_tests_from_journey_coverage: bool, none_type, optional

        :param test_suite_name: An optional custom name for the auto-created test suite.
        :type test_suite_name: str, none_type, optional
        """
        if include_tests_from_journey_coverage is not unset:
            kwargs["include_tests_from_journey_coverage"] = include_tests_from_journey_coverage
        if test_suite_name is not unset:
            kwargs["test_suite_name"] = test_suite_name
        super().__init__(kwargs)
