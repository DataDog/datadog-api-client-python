# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class IncidentCaseLinkDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "entity_id": (str,),
            "is_page": (bool,),
            "relationship": (str,),
        }

    attribute_map = {
        "entity_id": "entity_id",
        "is_page": "is_page",
        "relationship": "relationship",
    }

    def __init__(self_, entity_id: str, is_page: bool, relationship: str, **kwargs):
        """
        Attributes of a case link.

        :param entity_id: The entity identifier.
        :type entity_id: str

        :param is_page: Whether this is a page link.
        :type is_page: bool

        :param relationship: The relationship type.
        :type relationship: str
        """
        super().__init__(kwargs)

        self_.entity_id = entity_id
        self_.is_page = is_page
        self_.relationship = relationship
