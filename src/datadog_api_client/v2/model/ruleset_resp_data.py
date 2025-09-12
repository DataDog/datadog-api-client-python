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
    from datadog_api_client.v2.model.ruleset_resp_data_attributes import RulesetRespDataAttributes
    from datadog_api_client.v2.model.ruleset_resp_data_type import RulesetRespDataType


class RulesetRespData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ruleset_resp_data_attributes import RulesetRespDataAttributes
        from datadog_api_client.v2.model.ruleset_resp_data_type import RulesetRespDataType

        return {
            "attributes": (RulesetRespDataAttributes,),
            "id": (str,),
            "type": (RulesetRespDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: RulesetRespDataType,
        attributes: Union[RulesetRespDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``RulesetRespData`` object.

        :param attributes: The definition of ``RulesetRespDataAttributes`` object.
        :type attributes: RulesetRespDataAttributes, optional

        :param id: The ``RulesetRespData`` ``id``.
        :type id: str, optional

        :param type: Ruleset resource type.
        :type type: RulesetRespDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
