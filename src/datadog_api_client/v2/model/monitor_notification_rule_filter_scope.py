# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class MonitorNotificationRuleFilterScope(ModelNormal):
    validations = {
        "scope": {
            "max_length": 3000,
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "scope": (str,),
        }

    attribute_map = {
        "scope": "scope",
    }

    def __init__(self_, scope: str, **kwargs):
        """
        Filters monitor notifications using a scope expression over key:value pairs with boolean logic (AND, OR, NOT).

        :param scope: A scope expression composed by key:value pairs (e.g. ``service:foo`` ) with boolean operators (AND, OR, NOT) and parentheses for grouping.
        :type scope: str
        """
        super().__init__(kwargs)

        self_.scope = scope
