# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.relationship_to_organization_data import RelationshipToOrganizationData


class RelationshipToOrganizations(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.relationship_to_organization_data import RelationshipToOrganizationData

        return {
            "data": ([RelationshipToOrganizationData],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: List[RelationshipToOrganizationData], *args, **kwargs):
        """
        Relationship to organizations.

        :param data: Relationships to organization objects.
        :type data: [RelationshipToOrganizationData]
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.data = data
