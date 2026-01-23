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
    from datadog_api_client.v2.model.custom_rule_revision_input_attributes import CustomRuleRevisionInputAttributes
    from datadog_api_client.v2.model.custom_rule_revision_data_type import CustomRuleRevisionDataType


class CustomRuleRevisionRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule_revision_input_attributes import CustomRuleRevisionInputAttributes
        from datadog_api_client.v2.model.custom_rule_revision_data_type import CustomRuleRevisionDataType

        return {
            "attributes": (CustomRuleRevisionInputAttributes,),
            "id": (str,),
            "type": (CustomRuleRevisionDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[CustomRuleRevisionInputAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[CustomRuleRevisionDataType, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param attributes:
        :type attributes: CustomRuleRevisionInputAttributes, optional

        :param id: Revision identifier
        :type id: str, optional

        :param type: Resource type
        :type type: CustomRuleRevisionDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
