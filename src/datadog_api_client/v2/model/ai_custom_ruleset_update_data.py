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
    from datadog_api_client.v2.model.ai_custom_ruleset_update_attributes import AiCustomRulesetUpdateAttributes
    from datadog_api_client.v2.model.ai_custom_ruleset_data_type import AiCustomRulesetDataType


class AiCustomRulesetUpdateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ai_custom_ruleset_update_attributes import AiCustomRulesetUpdateAttributes
        from datadog_api_client.v2.model.ai_custom_ruleset_data_type import AiCustomRulesetDataType

        return {
            "attributes": (AiCustomRulesetUpdateAttributes,),
            "id": (str,),
            "type": (AiCustomRulesetDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[AiCustomRulesetUpdateAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[AiCustomRulesetDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Request data for updating an AI custom ruleset.

        :param attributes: Attributes for updating an AI custom ruleset.
        :type attributes: AiCustomRulesetUpdateAttributes, optional

        :param id: The ruleset identifier.
        :type id: str, optional

        :param type: AI custom ruleset resource type.
        :type type: AiCustomRulesetDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
