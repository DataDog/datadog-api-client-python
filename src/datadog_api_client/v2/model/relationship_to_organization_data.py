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
    from datadog_api_client.v2.model.organizations_type import OrganizationsType


class RelationshipToOrganizationData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.organizations_type import OrganizationsType

        return {
            "id": (str,),
            "type": (OrganizationsType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: OrganizationsType, **kwargs):
        """
        Relationship to organization object.

        :param id: ID of the organization.
        :type id: str

        :param type: Organizations resource type.
        :type type: OrganizationsType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
