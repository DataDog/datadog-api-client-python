# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentNotificationRuleConditionsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "field": (str,),
            "values": ([str],),
        }

    attribute_map = {
        "field": "field",
        "values": "values",
    }

    def __init__(self_, field: str, values: List[str], **kwargs):
        """
        A condition that must be met to trigger the notification rule.

        :param field: The incident field to evaluate
        :type field: str

        :param values: The value(s) to compare against. Multiple values are ``ORed`` together.
        :type values: [str]
        """
        super().__init__(kwargs)

        self_.field = field
        self_.values = values
