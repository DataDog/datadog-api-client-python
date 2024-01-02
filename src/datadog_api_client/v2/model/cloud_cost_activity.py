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
    from datadog_api_client.v2.model.cloud_cost_activity_attributes import CloudCostActivityAttributes
    from datadog_api_client.v2.model.cloud_cost_activity_type import CloudCostActivityType


class CloudCostActivity(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cloud_cost_activity_attributes import CloudCostActivityAttributes
        from datadog_api_client.v2.model.cloud_cost_activity_type import CloudCostActivityType

        return {
            "attributes": (CloudCostActivityAttributes,),
            "type": (CloudCostActivityType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(self_, attributes: CloudCostActivityAttributes, type: CloudCostActivityType, **kwargs):
        """
        Cloud Cost Activity.

        :param attributes: Attributes for Cloud Cost activity.
        :type attributes: CloudCostActivityAttributes

        :param type: Type of Cloud Cost Activity.
        :type type: CloudCostActivityType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
