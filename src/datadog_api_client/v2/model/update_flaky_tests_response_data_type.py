# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class UpdateFlakyTestsResponseDataType(ModelSimple):
    """
    The definition of `UpdateFlakyTestsResponseDataType` object.

    :param value: If omitted defaults to "update_flaky_test_state_response". Must be one of ["update_flaky_test_state_response"].
    :type value: str
    """

    allowed_values = {
        "update_flaky_test_state_response",
    }
    UPDATE_FLAKY_TEST_STATE_RESPONSE: ClassVar["UpdateFlakyTestsResponseDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


UpdateFlakyTestsResponseDataType.UPDATE_FLAKY_TEST_STATE_RESPONSE = UpdateFlakyTestsResponseDataType(
    "update_flaky_test_state_response"
)
