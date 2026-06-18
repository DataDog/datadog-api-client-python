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
    from datadog_api_client.v2.model.due_date_per_severity_item import DueDatePerSeverityItem
    from datadog_api_client.v2.model.due_date_from import DueDateFrom


class DueDateRuleAction(ModelNormal):
    validations = {
        "reason_description": {
            "max_length": 20000,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.due_date_per_severity_item import DueDatePerSeverityItem
        from datadog_api_client.v2.model.due_date_from import DueDateFrom

        return {
            "due_days_per_severity": ([DueDatePerSeverityItem],),
            "due_from": (DueDateFrom,),
            "reason_description": (str,),
        }

    attribute_map = {
        "due_days_per_severity": "due_days_per_severity",
        "due_from": "due_from",
        "reason_description": "reason_description",
    }

    def __init__(
        self_,
        due_days_per_severity: List[DueDatePerSeverityItem],
        due_from: DueDateFrom,
        reason_description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The action to take when the due date rule matches a finding.

        :param due_days_per_severity: A list of severity-to-due-date mappings. Each severity may appear at most once.
        :type due_days_per_severity: [DueDatePerSeverityItem]

        :param due_from: The reference point from which the due date is calculated. When ``fix_available`` is selected but not applicable to the finding type, ``first_seen`` is used instead.
        :type due_from: DueDateFrom

        :param reason_description: An optional description providing more context for the due date assignment.
        :type reason_description: str, optional
        """
        if reason_description is not unset:
            kwargs["reason_description"] = reason_description
        super().__init__(kwargs)

        self_.due_days_per_severity = due_days_per_severity
        self_.due_from = due_from
