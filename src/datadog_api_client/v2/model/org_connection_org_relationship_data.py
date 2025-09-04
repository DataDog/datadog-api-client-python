# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.org_connection_org_relationship_data_type import (
        OrgConnectionOrgRelationshipDataType,
    )


class OrgConnectionOrgRelationshipData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.org_connection_org_relationship_data_type import (
            OrgConnectionOrgRelationshipDataType,
        )

        return {
            "id": (str,),
            "name": (str,),
            "type": (OrgConnectionOrgRelationshipDataType,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        type: Union[OrgConnectionOrgRelationshipDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``OrgConnectionOrgRelationshipData`` object.

        :param id: Org UUID.
        :type id: str, optional

        :param name: Org name.
        :type name: str, optional

        :param type: The type of the organization relationship.
        :type type: OrgConnectionOrgRelationshipDataType, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
