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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.condition_operator import ConditionOperator


class ConditionRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.condition_operator import ConditionOperator

        return {
            "attribute": (str,),
            "operator": (ConditionOperator,),
            "saved_filter_id": (UUID,),
            "value": ([str],),
        }

    attribute_map = {
        "attribute": "attribute",
        "operator": "operator",
        "saved_filter_id": "saved_filter_id",
        "value": "value",
    }

    def __init__(
        self_,
        attribute: Union[str, UnsetType] = unset,
        operator: Union[ConditionOperator, UnsetType] = unset,
        saved_filter_id: Union[UUID, UnsetType] = unset,
        value: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Condition request payload for targeting rules. A condition is either an inline
        predicate with ``operator`` , ``attribute`` , and ``value`` , or a reference to a
        saved filter with ``saved_filter_id``. The two shapes are mutually exclusive.

        :param attribute: The user or request attribute to evaluate. Required for inline conditions; omit when ``saved_filter_id`` is set.
        :type attribute: str, optional

        :param operator: The operator used in a targeting condition.
        :type operator: ConditionOperator, optional

        :param saved_filter_id: The ID of a saved filter to reference as this condition. Mutually exclusive
            with ``operator`` , ``attribute`` , and ``value``. When set, the saved filter's
            targeting rules are evaluated in place of an inline predicate.
        :type saved_filter_id: UUID, optional

        :param value: Values used by the selected operator. Required for inline conditions; omit when ``saved_filter_id`` is set.
        :type value: [str], optional
        """
        if attribute is not unset:
            kwargs["attribute"] = attribute
        if operator is not unset:
            kwargs["operator"] = operator
        if saved_filter_id is not unset:
            kwargs["saved_filter_id"] = saved_filter_id
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
