# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class SecurityAgentInvestigationRuleTuningCondition(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "field": (str,),
            "value": (str,),
        }

    attribute_map = {
        "field": "field",
        "value": "value",
    }

    def __init__(self_, field: str, value: str, **kwargs):
        """
        A condition of a rule tuning suggestion.

        :param field: Attribute the condition checks.
        :type field: str

        :param value: Value the attribute is compared with.
        :type value: str
        """
        super().__init__(kwargs)

        self_.field = field
        self_.value = value
