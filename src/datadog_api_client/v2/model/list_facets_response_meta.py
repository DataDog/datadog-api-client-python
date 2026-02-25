# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class ListFacetsResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_entities": (int,),
        }

    attribute_map = {
        "total_entities": "total_entities",
    }

    def __init__(self_, total_entities: int, **kwargs):
        """
        Metadata for facets response.

        :param total_entities: Total number of entities.
        :type total_entities: int
        """
        super().__init__(kwargs)

        self_.total_entities = total_entities
