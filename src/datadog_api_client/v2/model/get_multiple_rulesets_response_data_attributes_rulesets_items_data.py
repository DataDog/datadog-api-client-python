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
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_data_type import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType,
    )


class GetMultipleRulesetsResponseDataAttributesRulesetsItemsData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_data_type import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType,
        )

        return {
            "id": (str,),
            "type": (GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param id:
        :type id: str, optional

        :param type: Rulesets resource type.
        :type type: GetMultipleRulesetsResponseDataAttributesRulesetsItemsDataType
        """
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
