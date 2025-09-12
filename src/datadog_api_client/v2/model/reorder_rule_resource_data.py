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
    from datadog_api_client.v2.model.reorder_rule_resource_data_type import ReorderRuleResourceDataType


class ReorderRuleResourceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.reorder_rule_resource_data_type import ReorderRuleResourceDataType

        return {
            "id": (str,),
            "type": (ReorderRuleResourceDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: ReorderRuleResourceDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``ReorderRuleResourceData`` object.

        :param id: The ``ReorderRuleResourceData`` ``id``.
        :type id: str, optional

        :param type: Arbitrary rule resource type.
        :type type: ReorderRuleResourceDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
