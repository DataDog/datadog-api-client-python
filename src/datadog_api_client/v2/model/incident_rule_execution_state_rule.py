# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


class IncidentRuleExecutionStateRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "last_executed_at": (datetime, none_type),
            "rule_uuid": (UUID,),
        }

    attribute_map = {
        "last_executed_at": "last_executed_at",
        "rule_uuid": "rule_uuid",
    }

    def __init__(self_, rule_uuid: UUID, last_executed_at: Union[datetime, none_type, UnsetType] = unset, **kwargs):
        """
        A rule in a batch request.

        :param last_executed_at: Timestamp of the last rule execution.
        :type last_executed_at: datetime, none_type, optional

        :param rule_uuid: The rule identifier.
        :type rule_uuid: UUID
        """
        if last_executed_at is not unset:
            kwargs["last_executed_at"] = last_executed_at
        super().__init__(kwargs)

        self_.rule_uuid = rule_uuid
