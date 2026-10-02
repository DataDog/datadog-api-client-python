# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_targeting_rules_items_conditions_items import (
        ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItemsConditionsItems,
    )


class ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.experiments_public_protocol_response_data_attributes_targeting_rules_items_conditions_items import (
            ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItemsConditionsItems,
        )

        return {
            "conditions": ([ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItemsConditionsItems],),
        }

    attribute_map = {
        "conditions": "conditions",
    }

    def __init__(
        self_,
        conditions: Union[
            List[ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItemsConditionsItems], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        A targeting rule supplied by the protocol.

        :param conditions: Conditions that define this targeting rule.
        :type conditions: [ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItemsConditionsItems], optional
        """
        if conditions is not unset:
            kwargs["conditions"] = conditions
        super().__init__(kwargs)
