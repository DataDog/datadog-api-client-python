# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class FlakyTestType(ModelSimple):
    """
    The type of the flaky test from Flaky Test Management.

    :param value: If omitted defaults to "flaky_test". Must be one of ["flaky_test"].
    :type value: str
    """

    allowed_values = {
        "flaky_test",
    }
    FLAKY_TEST: ClassVar["FlakyTestType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


FlakyTestType.FLAKY_TEST = FlakyTestType("flaky_test")
