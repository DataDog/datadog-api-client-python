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
    from datadog_api_client.v2.model.rule_version_history import RuleVersionHistory
    from datadog_api_client.v2.model.get_rule_version_history_data_type import GetRuleVersionHistoryDataType


class GetRuleVersionHistoryData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rule_version_history import RuleVersionHistory
        from datadog_api_client.v2.model.get_rule_version_history_data_type import GetRuleVersionHistoryDataType

        return {
            "attributes": (RuleVersionHistory,),
            "id": (str,),
            "type": (GetRuleVersionHistoryDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RuleVersionHistory, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[GetRuleVersionHistoryDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for the rule version history.

        :param attributes: Response object containing the version history of a rule.
        :type attributes: RuleVersionHistory, optional

        :param id: ID of the rule.
        :type id: str, optional

        :param type: Type of data.
        :type type: GetRuleVersionHistoryDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
