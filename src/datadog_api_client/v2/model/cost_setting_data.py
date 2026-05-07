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
    from datadog_api_client.v2.model.cost_setting_data_attributes import CostSettingDataAttributes
    from datadog_api_client.v2.model.cost_setting_type import CostSettingType


class CostSettingData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_setting_data_attributes import CostSettingDataAttributes
        from datadog_api_client.v2.model.cost_setting_type import CostSettingType

        return {
            "attributes": (CostSettingDataAttributes,),
            "id": (str,),
            "type": (CostSettingType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CostSettingDataAttributes, id: str, type: CostSettingType, **kwargs):
        """
        Cost setting data object.

        :param attributes: Attributes for a cost setting.
        :type attributes: CostSettingDataAttributes

        :param id: The unique identifier of the setting.
        :type id: str

        :param type: Cost setting resource type.
        :type type: CostSettingType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
