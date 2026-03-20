# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TestOptimizationServiceSettingsType(ModelSimple):
    """
    JSON:API type for service settings response. The value must always be `test_optimization_service_settings`.

    :param value: If omitted defaults to "test_optimization_service_settings". Must be one of ["test_optimization_service_settings"].
    :type value: str
    """

    allowed_values = {
        "test_optimization_service_settings",
    }
    TEST_OPTIMIZATION_SERVICE_SETTINGS: ClassVar["TestOptimizationServiceSettingsType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TestOptimizationServiceSettingsType.TEST_OPTIMIZATION_SERVICE_SETTINGS = TestOptimizationServiceSettingsType(
    "test_optimization_service_settings"
)
