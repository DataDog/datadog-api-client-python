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
    from datadog_api_client.v2.model.update_ruleset_request_data_attributes import UpdateRulesetRequestDataAttributes
    from datadog_api_client.v2.model.update_ruleset_request_data_type import UpdateRulesetRequestDataType


class UpdateRulesetRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_ruleset_request_data_attributes import (
            UpdateRulesetRequestDataAttributes,
        )
        from datadog_api_client.v2.model.update_ruleset_request_data_type import UpdateRulesetRequestDataType

        return {
            "attributes": (UpdateRulesetRequestDataAttributes,),
            "id": (str,),
            "type": (UpdateRulesetRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: UpdateRulesetRequestDataType,
        attributes: Union[UpdateRulesetRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UpdateRulesetRequestData`` object.

        :param attributes: The definition of ``UpdateRulesetRequestDataAttributes`` object.
        :type attributes: UpdateRulesetRequestDataAttributes, optional

        :param id: The ``UpdateRulesetRequestData`` ``id``.
        :type id: str, optional

        :param type: Update ruleset resource type.
        :type type: UpdateRulesetRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
