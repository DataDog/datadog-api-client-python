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
    from datadog_api_client.v2.model.test_optimization_service_settings_attributes import (
        TestOptimizationServiceSettingsAttributes,
    )
    from datadog_api_client.v2.model.test_optimization_service_settings_type import TestOptimizationServiceSettingsType


class TestOptimizationServiceSettingsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_service_settings_attributes import (
            TestOptimizationServiceSettingsAttributes,
        )
        from datadog_api_client.v2.model.test_optimization_service_settings_type import (
            TestOptimizationServiceSettingsType,
        )

        return {
            "attributes": (TestOptimizationServiceSettingsAttributes,),
            "id": (str,),
            "type": (TestOptimizationServiceSettingsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[TestOptimizationServiceSettingsAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[TestOptimizationServiceSettingsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data object for Test Optimization service settings response.

        :param attributes: Attributes for Test Optimization service settings.
        :type attributes: TestOptimizationServiceSettingsAttributes, optional

        :param id: Unique identifier for the service settings.
        :type id: str, optional

        :param type: JSON:API type for service settings response. The value must always be ``test_optimization_service_settings``.
        :type type: TestOptimizationServiceSettingsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
