# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
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
            "updated_at": (datetime,),
            "value": ([str],),
        }

    attribute_map = {
        "attribute": "attribute",
        "created_at": "created_at",
        "id": "id",
        "operator": "operator",
        "updated_at": "updated_at",
        "value": "value",
    }

    def __init__(
        self_,
        attribute: str,
        created_at: datetime,
        id: UUID,
        operator: ConditionOperator,
        updated_at: datetime,
        value: List[str],
        **kwargs,
    ):
        """
        Targeting condition details.

        :param attribute: The user or request attribute to evaluate.
        :type attribute: str

        :param created_at: The timestamp when the condition was created.
        :type created_at: datetime

        :param id: The unique identifier of the condition.
        :type id: UUID

        :param operator: The operator used in a targeting condition.
        :type operator: ConditionOperator

        :param updated_at: The timestamp when the condition was last updated.
        :type updated_at: datetime

        :param value: Values used by the selected operator.
        :type value: [str]
        """
        super().__init__(kwargs)

        self_.attribute = attribute
        self_.created_at = created_at
        self_.id = id
        self_.operator = operator
        self_.updated_at = updated_at
        self_.value = value
