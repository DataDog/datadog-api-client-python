# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_data import (
        TestOptimizationDeleteServiceSettingsRequestData,
    )


class TestOptimizationDeleteServiceSettingsRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_data import (
            TestOptimizationDeleteServiceSettingsRequestData,
        )

        return {
            "data": (TestOptimizationDeleteServiceSettingsRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: TestOptimizationDeleteServiceSettingsRequestData, **kwargs):
        """
        Request object for deleting Test Optimization service settings.

        :param data: Data object for delete service settings request.
        :type data: TestOptimizationDeleteServiceSettingsRequestData
        """
        super().__init__(kwargs)

        self_.data = data
