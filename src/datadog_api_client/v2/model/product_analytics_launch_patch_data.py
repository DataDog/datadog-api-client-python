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
    from datadog_api_client.v2.model.product_analytics_launch_patch_attributes import (
        ProductAnalyticsLaunchPatchAttributes,
    )
    from datadog_api_client.v2.model.product_analytics_launch_type import ProductAnalyticsLaunchType


class ProductAnalyticsLaunchPatchData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_launch_patch_attributes import (
            ProductAnalyticsLaunchPatchAttributes,
        )
        from datadog_api_client.v2.model.product_analytics_launch_type import ProductAnalyticsLaunchType

        return {
            "attributes": (ProductAnalyticsLaunchPatchAttributes,),
            "id": (str,),
            "type": (ProductAnalyticsLaunchType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: ProductAnalyticsLaunchPatchAttributes, id: str, type: ProductAnalyticsLaunchType, **kwargs
    ):
        """
        Data of the launch update.

        :param attributes: Attributes to update on a launch. Fields that are not set are left unchanged, and ``null`` clears a nullable
            field.
            Setting a non-empty ``feature_flag_id`` clears the stored ``feature_flag_key`` when ``feature_flag_key`` is not set.
        :type attributes: ProductAnalyticsLaunchPatchAttributes

        :param id: UUID of the launch. It must match the ID in the path.
        :type id: str

        :param type: Launch resource type.
        :type type: ProductAnalyticsLaunchType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
