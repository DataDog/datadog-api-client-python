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
    from datadog_api_client.v2.model.condition import Condition


class TargetingRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.condition import Condition

        return {
            "conditions": ([Condition],),
            "created_at": (datetime,),
            "id": (UUID,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "conditions": "conditions",
        "created_at": "created_at",
        "id": "id",
        "updated_at": "updated_at",
    }

    def __init__(self_, conditions: List[Condition], created_at: datetime, id: UUID, updated_at: datetime, **kwargs):
        """
        Targeting rule details.

        :param conditions: Conditions evaluated by this targeting rule.
        :type conditions: [Condition]

        :param created_at: The timestamp when the targeting rule was created.
        :type created_at: datetime

        :param id: The unique identifier of the targeting rule.
        :type id: UUID

        :param updated_at: The timestamp when the targeting rule was last updated.
        :type updated_at: datetime
        """
        super().__init__(kwargs)

        self_.conditions = conditions
        self_.created_at = created_at
        self_.id = id
        self_.updated_at = updated_at
