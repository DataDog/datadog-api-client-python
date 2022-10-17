# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.organization_attributes import OrganizationAttributes

if TYPE_CHECKING:
    from datadog_api_client.v2.model.organizations_type import OrganizationsType


@dataclass
class OrganizationJSON:
    id: str
    created_at: Union[datetime, UnsetType] = unset
    description: Union[str, UnsetType] = unset
    disabled: Union[bool, UnsetType] = unset
    modified_at: Union[datetime, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    public_id: Union[str, UnsetType] = unset
    sharing: Union[str, UnsetType] = unset
    url: Union[str, UnsetType] = unset


class Organization(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.organizations_type import OrganizationsType

        return {
            "attributes": (OrganizationAttributes,),
            "id": (str,),
            "type": (OrganizationsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    json_api_model = OrganizationJSON

    def __init__(
        self_,
        type: OrganizationsType,
        attributes: Union[OrganizationAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Organization object.

        :param attributes: Attributes of the organization.
        :type attributes: OrganizationAttributes, optional

        :param id: ID of the organization.
        :type id: str, optional

        :param type: Organizations resource type.
        :type type: OrganizationsType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
