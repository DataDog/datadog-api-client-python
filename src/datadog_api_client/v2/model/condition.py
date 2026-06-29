# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.condition_operator import ConditionOperator


class Condition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.condition_operator import ConditionOperator

        return {
            "attribute": (str,),
            "created_at": (datetime,),
            "id": (UUID,),
            "operator": (ConditionOperator,),
            "saved_filter_id": (UUID, none_type),
            "updated_at": (datetime,),
            "value": ([str],),
        }

    attribute_map = {
        "attribute": "attribute",
        "created_at": "created_at",
        "id": "id",
        "operator": "operator",
        "saved_filter_id": "saved_filter_id",
        "updated_at": "updated_at",
        "value": "value",
    }

    def __init__(
        self_,
        created_at: datetime,
        id: UUID,
        updated_at: datetime,
        attribute: Union[str, UnsetType] = unset,
        operator: Union[ConditionOperator, UnsetType] = unset,
        saved_filter_id: Union[UUID, none_type, UnsetType] = unset,
        value: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Targeting condition details. A condition is either an inline
        predicate with ``operator`` , ``attribute`` , and ``value`` , or a reference to a
        saved filter with ``saved_filter_id``. The inline fields are omitted for saved-filter
        references.

        :param attribute: The user or request attribute to evaluate. Omitted for saved-filter references.
        :type attribute: str, optional

        :param created_at: The timestamp when the condition was created.
        :type created_at: datetime

        :param id: The unique identifier of the condition.
        :type id: UUID

        :param operator: The operator used in a targeting condition.
        :type operator: ConditionOperator, optional

        :param saved_filter_id: The ID of the saved filter referenced by this condition, or null for inline conditions.
        :type saved_filter_id: UUID, none_type, optional

        :param updated_at: The timestamp when the condition was last updated.
        :type updated_at: datetime

        :param value: Values used by the selected operator. Omitted for saved-filter references.
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

        self_.created_at = created_at
        self_.id = id
        self_.updated_at = updated_at
