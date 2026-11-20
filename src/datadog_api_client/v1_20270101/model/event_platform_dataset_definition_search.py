# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class EventPlatformDatasetDefinitionSearch(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        return {
            "query": (str,),
        }

    attribute_map = {
        "query": "query",
    }

    def __init__(self_, query: str, **kwargs):
        """
        Test-only generated schema for the dashboard versioning proof of concept.

        :param query: Test-only generated schema for the dashboard versioning proof of concept.
        :type query: str
        """
        super().__init__(kwargs)

        self_.query = query
