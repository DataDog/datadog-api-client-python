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
    from datadog_api_client.v2.model.test_optimization_update_service_settings_request_attributes import (
        TestOptimizationUpdateServiceSettingsRequestAttributes,
    )
    from datadog_api_client.v2.model.test_optimization_update_service_settings_request_data_type import (
        TestOptimizationUpdateServiceSettingsRequestDataType,
    )


class TestOptimizationUpdateServiceSettingsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_update_service_settings_request_attributes import (
            TestOptimizationUpdateServiceSettingsRequestAttributes,
        )
        from datadog_api_client.v2.model.test_optimization_update_service_settings_request_data_type import (
            TestOptimizationUpdateServiceSettingsRequestDataType,
        )

        return {
            "attributes": (TestOptimizationUpdateServiceSettingsRequestAttributes,),
            "type": (TestOptimizationUpdateServiceSettingsRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TestOptimizationUpdateServiceSettingsRequestAttributes,
        type: TestOptimizationUpdateServiceSettingsRequestDataType,
        **kwargs,
    ):
        """
        Data object for update service settings request.

        :param attributes: Attributes for updating Test Optimization service settings.
            All non-required fields are optional; only provided fields will be updated.
        :type attributes: TestOptimizationUpdateServiceSettingsRequestAttributes

        :param type: JSON:API type for update service settings request.
            The value must always be ``test_optimization_update_service_settings_request``.
        :type type: TestOptimizationUpdateServiceSettingsRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
