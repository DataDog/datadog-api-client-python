# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class CaseGroupBy(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "field": (str,),
        }

    attribute_map = {
        "field": "field",
    }

    def __init__(self_, field: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param field: Test-only generated schema for the dashboard versioning proof of concept.
        :type field: str
        """
        super().__init__(kwargs)

        self_.field = field
