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
    from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_attributes import (
        TestOptimizationDeleteServiceSettingsRequestAttributes,
    )
    from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_data_type import (
        TestOptimizationDeleteServiceSettingsRequestDataType,
    )


class TestOptimizationDeleteServiceSettingsRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_attributes import (
            TestOptimizationDeleteServiceSettingsRequestAttributes,
        )
        from datadog_api_client.v2.model.test_optimization_delete_service_settings_request_data_type import (
            TestOptimizationDeleteServiceSettingsRequestDataType,
        )

        return {
            "attributes": (TestOptimizationDeleteServiceSettingsRequestAttributes,),
            "type": (TestOptimizationDeleteServiceSettingsRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: TestOptimizationDeleteServiceSettingsRequestAttributes,
        type: TestOptimizationDeleteServiceSettingsRequestDataType,
        **kwargs,
    ):
        """
        Data object for delete service settings request.

        :param attributes: Attributes for deleting Test Optimization service settings.
        :type attributes: TestOptimizationDeleteServiceSettingsRequestAttributes

        :param type: JSON:API type for delete service settings request.
            The value must always be ``test_optimization_delete_service_settings_request``.
        :type type: TestOptimizationDeleteServiceSettingsRequestDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
