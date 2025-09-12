# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FlakyTestsSearchRequestDataType(ModelSimple):
    """
    The definition of `FlakyTestsSearchRequestDataType` object.

    :param value: If omitted defaults to "search_flaky_tests_request". Must be one of ["search_flaky_tests_request"].
    :type value: str
    """

    allowed_values = {
        "search_flaky_tests_request",
    }
    SEARCH_FLAKY_TESTS_REQUEST: ClassVar["FlakyTestsSearchRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FlakyTestsSearchRequestDataType.SEARCH_FLAKY_TESTS_REQUEST = FlakyTestsSearchRequestDataType(
    "search_flaky_tests_request"
)
