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
    from datadog_api_client.v2.model.ruleset_status_resp_data_attributes import RulesetStatusRespDataAttributes
    from datadog_api_client.v2.model.ruleset_status_resp_data_type import RulesetStatusRespDataType


class RulesetStatusRespData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ruleset_status_resp_data_attributes import RulesetStatusRespDataAttributes
        from datadog_api_client.v2.model.ruleset_status_resp_data_type import RulesetStatusRespDataType

        return {
            "attributes": (RulesetStatusRespDataAttributes,),
            "id": (str,),
            "type": (RulesetStatusRespDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RulesetStatusRespDataAttributes, id: str, type: RulesetStatusRespDataType, **kwargs
    ):
        """
        The definition of ``RulesetStatusRespData`` object.

        :param attributes: The definition of ``RulesetStatusRespDataAttributes`` object.
        :type attributes: RulesetStatusRespDataAttributes

        :param id: The unique identifier of the ruleset.
        :type id: str

        :param type: Ruleset status resource type.
        :type type: RulesetStatusRespDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
