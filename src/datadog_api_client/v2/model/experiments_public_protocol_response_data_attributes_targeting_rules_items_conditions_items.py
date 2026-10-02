# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ExperimentsPublicProtocolResponseDataAttributesTargetingRulesItemsConditionsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "attribute": (str,),
            "operator": (str,),
            "order_position": (int,),
            "saved_filter_id": (str,),
            "value": ([str],),
        }

    attribute_map = {
        "attribute": "attribute",
        "operator": "operator",
        "order_position": "order_position",
        "saved_filter_id": "saved_filter_id",
        "value": "value",
    }

    def __init__(
        self_,
        attribute: Union[str, UnsetType] = unset,
        operator: Union[str, UnsetType] = unset,
        order_position: Union[int, UnsetType] = unset,
        saved_filter_id: Union[str, UnsetType] = unset,
        value: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        One condition in a protocol targeting rule.

        :param attribute: Subject attribute evaluated by the targeting condition.
        :type attribute: str, optional

        :param operator: Comparison applied to the subject attribute.
        :type operator: str, optional

        :param order_position: Position of this entry in the ordered configuration.
        :type order_position: int, optional

        :param saved_filter_id: ID of the saved filter used by this targeting condition.
        :type saved_filter_id: str, optional

        :param value: Values compared with the subject attribute in this condition.
        :type value: [str], optional
        """
        if attribute is not unset:
            kwargs["attribute"] = attribute
        if operator is not unset:
            kwargs["operator"] = operator
        if order_position is not unset:
            kwargs["order_position"] = order_position
        if saved_filter_id is not unset:
            kwargs["saved_filter_id"] = saved_filter_id
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
