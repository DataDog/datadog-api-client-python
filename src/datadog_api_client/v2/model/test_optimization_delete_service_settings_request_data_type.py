# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelSimple,
    cached_property,
)

from typing import ClassVar


class TestOptimizationDeleteServiceSettingsRequestDataType(ModelSimple):
    """
    JSON:API type for delete service settings request. The value must always be `test_optimization_delete_service_settings_request`.

    :param value: If omitted defaults to "test_optimization_delete_service_settings_request". Must be one of ["test_optimization_delete_service_settings_request"].
    :type value: str
    """

    allowed_values = {
        "test_optimization_delete_service_settings_request",
    }
    TEST_OPTIMIZATION_DELETE_SERVICE_SETTINGS_REQUEST: ClassVar["TestOptimizationDeleteServiceSettingsRequestDataType"]

    @cached_property
    def openapi_types(_):
        return {
            "value": (str,),
        }


TestOptimizationDeleteServiceSettingsRequestDataType.TEST_OPTIMIZATION_DELETE_SERVICE_SETTINGS_REQUEST = (
    TestOptimizationDeleteServiceSettingsRequestDataType("test_optimization_delete_service_settings_request")
)
