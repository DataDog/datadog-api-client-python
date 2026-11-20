# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CohortScope20270101TargetOneOf4454865216(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "type": (CohortScopeTargetAggregationType,),
            "value": (CohortScopeTargetAnyOfAnyOfItemValue,),
        }

    attribute_map = {
        "type": "type",
        "value": "value",
    }

    def __init__(self_, type: CohortScopeTargetAggregationType, value: CohortScopeTargetAnyOfAnyOfItemValue, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param type: Test-only generated schema for the dashboard versioning proof of concept.
        :type type: CohortScopeTargetAggregationType

        :param value: Test-only generated schema for the dashboard versioning proof of concept.
        :type value: CohortScopeTargetAnyOfAnyOfItemValue
        """
        super().__init__(kwargs)

        self_.type = type
        self_.value = value
