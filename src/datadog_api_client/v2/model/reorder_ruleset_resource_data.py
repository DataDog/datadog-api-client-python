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
    from datadog_api_client.v2.model.reorder_ruleset_resource_data_type import ReorderRulesetResourceDataType


class ReorderRulesetResourceData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.reorder_ruleset_resource_data_type import ReorderRulesetResourceDataType

        return {
            "id": (str,),
            "type": (ReorderRulesetResourceDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, type: ReorderRulesetResourceDataType, id: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``ReorderRulesetResourceData`` object.

        :param id: The ``ReorderRulesetResourceData`` ``id``.
        :type id: str, optional

        :param type: Ruleset resource type.
        :type type: ReorderRulesetResourceDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
