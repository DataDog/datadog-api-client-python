# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.due_date_severity import DueDateSeverity


class DueDatePerSeverityItem(ModelNormal):
    validations = {
        "due_in_days": {
            "inclusive_maximum": 365,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.due_date_severity import DueDateSeverity

        return {
            "due_in_days": (int,),
            "severity": (DueDateSeverity,),
        }

    attribute_map = {
        "due_in_days": "due_in_days",
        "severity": "severity",
    }

    def __init__(self_, due_in_days: int, severity: DueDateSeverity, **kwargs):
        """
        A mapping of a severity level to the number of days until a finding is due.

        :param due_in_days: The number of days from the reference point until the finding is due.
        :type due_in_days: int

        :param severity: A severity level used to configure due date thresholds.
        :type severity: DueDateSeverity
        """
        super().__init__(kwargs)

        self_.due_in_days = due_in_days
        self_.severity = severity
