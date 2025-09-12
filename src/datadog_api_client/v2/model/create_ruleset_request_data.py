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
    from datadog_api_client.v2.model.create_ruleset_request_data_attributes import CreateRulesetRequestDataAttributes
    from datadog_api_client.v2.model.create_ruleset_request_data_type import CreateRulesetRequestDataType


class CreateRulesetRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_ruleset_request_data_attributes import (
            CreateRulesetRequestDataAttributes,
        )
        from datadog_api_client.v2.model.create_ruleset_request_data_type import CreateRulesetRequestDataType

        return {
            "attributes": (CreateRulesetRequestDataAttributes,),
            "id": (str,),
            "type": (CreateRulesetRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: CreateRulesetRequestDataType,
        attributes: Union[CreateRulesetRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateRulesetRequestData`` object.

        :param attributes: The definition of ``CreateRulesetRequestDataAttributes`` object.
        :type attributes: CreateRulesetRequestDataAttributes, optional

        :param id: The ``CreateRulesetRequestData`` ``id``.
        :type id: str, optional

        :param type: Create ruleset resource type.
        :type type: CreateRulesetRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
