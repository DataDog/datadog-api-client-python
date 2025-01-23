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
    from datadog_api_client.v2.model.create_inbox_rule_parameters_data import CreateInboxRuleParametersData


class CreateInboxRuleParameters(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_inbox_rule_parameters_data import CreateInboxRuleParametersData

        return {
            "data": (CreateInboxRuleParametersData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[CreateInboxRuleParametersData, UnsetType] = unset, **kwargs):
        """
        Body of the inbox rule create request

        :param data: Data of the inbox rule create request: the rule type, and the rule attributes. All fields are required.
        :type data: CreateInboxRuleParametersData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
