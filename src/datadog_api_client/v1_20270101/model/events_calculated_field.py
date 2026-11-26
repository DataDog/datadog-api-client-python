# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EventsCalculatedField(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "expression": (str,),
            "name": (str,),
        }

    attribute_map = {
        "expression": "expression",
        "name": "name",
    }

    def __init__(self_, expression: str, name: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param expression: Test-only generated schema for the dashboard versioning proof of concept.
        :type expression: str

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str
        """
        super().__init__(kwargs)

        self_.expression = expression
        self_.name = name
