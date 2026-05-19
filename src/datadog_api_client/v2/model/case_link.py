# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.case_link_attributes import CaseLinkAttributes
    from datadog_api_client.v2.model.case_link_resource_type import CaseLinkResourceType


class CaseLink(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.case_link_attributes import CaseLinkAttributes
        from datadog_api_client.v2.model.case_link_resource_type import CaseLinkResourceType

        return {
            "attributes": (CaseLinkAttributes,),
            "id": (str,),
            "type": (CaseLinkResourceType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, attributes: CaseLinkAttributes, id: str, type: CaseLinkResourceType, **kwargs):
        """
        A directional link representing a relationship between two entities. At least one entity must be a case.

        :param attributes: Attributes describing a directional relationship between two entities (cases, incidents, or pages).
        :type attributes: CaseLinkAttributes

        :param id: The case link identifier.
        :type id: str

        :param type: JSON:API resource type for case links.
        :type type: CaseLinkResourceType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
