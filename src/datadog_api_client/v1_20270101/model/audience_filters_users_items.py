# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class AudienceFiltersUsersItems(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "query": (str,),
        }

    attribute_map = {
        "name": "name",
        "query": "query",
    }

    def __init__(self_, name: str, query: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param name: Test-only generated schema for the dashboard versioning proof of concept.
        :type name: str

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str
        """
        super().__init__(kwargs)

        self_.name = name
        self_.query = query
