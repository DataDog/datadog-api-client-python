# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.list_external_user_group_response_resources_items_members_items import (
        ListExternalUserGroupResponseResourcesItemsMembersItems,
    )
    from datadog_api_client.v2.model.external_user_group_meta import ExternalUserGroupMeta


class ListExternalUserGroupResponseResourcesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.list_external_user_group_response_resources_items_members_items import (
            ListExternalUserGroupResponseResourcesItemsMembersItems,
        )
        from datadog_api_client.v2.model.external_user_group_meta import ExternalUserGroupMeta

        return {
            "display_name": (str,),
            "external_id": (str,),
            "id": (str,),
            "members": ([ListExternalUserGroupResponseResourcesItemsMembersItems],),
            "meta": (ExternalUserGroupMeta,),
            "schemas": ([str],),
        }

    attribute_map = {
        "display_name": "displayName",
        "external_id": "externalId",
        "id": "id",
        "members": "members",
        "meta": "meta",
        "schemas": "schemas",
    }

    def __init__(
        self_,
        display_name: Union[str, UnsetType] = unset,
        external_id: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        members: Union[List[ListExternalUserGroupResponseResourcesItemsMembersItems], UnsetType] = unset,
        meta: Union[ExternalUserGroupMeta, UnsetType] = unset,
        schemas: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        SCIM resources returned in response to a List SCIM groups request.

        :param display_name: A human-readable name for the group.
        :type display_name: str, optional

        :param external_id: An identifier for the resource as defined by the provisioning client.
        :type external_id: str, optional

        :param id: The identifier of the resource. Not required when creating a group.
        :type id: str, optional

        :param members: The ``items`` ``members``.
        :type members: [ListExternalUserGroupResponseResourcesItemsMembersItems], optional

        :param meta: Metadata associated with a SCIM group.
        :type meta: ExternalUserGroupMeta, optional

        :param schemas: SCIM group JSON Schemas.
        :type schemas: [str], optional
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if external_id is not unset:
            kwargs["external_id"] = external_id
        if id is not unset:
            kwargs["id"] = id
        if members is not unset:
            kwargs["members"] = members
        if meta is not unset:
            kwargs["meta"] = meta
        if schemas is not unset:
            kwargs["schemas"] = schemas
        super().__init__(kwargs)
