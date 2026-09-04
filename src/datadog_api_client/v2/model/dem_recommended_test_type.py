# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class DemRecommendedTestType(ModelSimple):
    """
    The type identifier for a recommended synthetic test.

    :param value: If omitted defaults to "recommended_tests". Must be one of ["recommended_tests"].
    :type value: str
    """

    allowed_values = {
        "recommended_tests",
    }
    RECOMMENDED_TESTS: ClassVar["DemRecommendedTestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


DemRecommendedTestType.RECOMMENDED_TESTS = DemRecommendedTestType("recommended_tests")
