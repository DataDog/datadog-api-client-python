# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.test_optimization_service_settings_data import TestOptimizationServiceSettingsData


class TestOptimizationServiceSettingsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_service_settings_data import (
            TestOptimizationServiceSettingsData,
        )

        return {
            "data": (TestOptimizationServiceSettingsData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[TestOptimizationServiceSettingsData, UnsetType] = unset, **kwargs):
        """
        Response object containing Test Optimization service settings.

        :param data: Data object for Test Optimization service settings response.
        :type data: TestOptimizationServiceSettingsData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
