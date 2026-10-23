# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_protocol_condition_input import ExperimentsProtocolConditionInput


class ExperimentsProtocolTargetingRuleInput(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_protocol_condition_input import ExperimentsProtocolConditionInput

        return {
            "conditions": ([ExperimentsProtocolConditionInput], none_type),
        }

    attribute_map = {
        "conditions": "conditions",
    }

    def __init__(
        self_, conditions: Union[List[ExperimentsProtocolConditionInput], none_type, UnsetType] = unset, **kwargs
    ):
        """
        A targeting rule in the protocol template.

        :param conditions: Conditions in this rule.
        :type conditions: [ExperimentsProtocolConditionInput], none_type, optional
        """
        if conditions is not unset:
            kwargs["conditions"] = conditions
        super().__init__(kwargs)
