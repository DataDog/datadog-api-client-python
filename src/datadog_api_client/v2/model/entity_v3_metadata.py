# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.entity_v3_metadata_additional_owners_items import (
        EntityV3MetadataAdditionalOwnersItems,
    )
    from datadog_api_client.v2.model.entity_v3_metadata_contacts_items import EntityV3MetadataContactsItems
    from datadog_api_client.v2.model.entity_v3_metadata_links_items import EntityV3MetadataLinksItems


class EntityV3Metadata(ModelNormal):
    validations = {
        "id": {
            "min_length": 1,
        },
        "name": {
            "min_length": 1,
        },
        "namespace": {
            "min_length": 1,
        },
    }

    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.entity_v3_metadata_additional_owners_items import (
            EntityV3MetadataAdditionalOwnersItems,
        )
        from datadog_api_client.v2.model.entity_v3_metadata_contacts_items import EntityV3MetadataContactsItems
        from datadog_api_client.v2.model.entity_v3_metadata_links_items import EntityV3MetadataLinksItems

        return {
            "additional_owners": ([EntityV3MetadataAdditionalOwnersItems],),
            "contacts": ([EntityV3MetadataContactsItems],),
            "description": (str,),
            "display_name": (str,),
            "id": (str,),
            "inherit_from": (str,),
            "links": ([EntityV3MetadataLinksItems],),
            "managed": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "name": (str,),
            "namespace": (str,),
            "owner": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "additional_owners": "additionalOwners",
        "contacts": "contacts",
        "description": "description",
        "display_name": "displayName",
        "id": "id",
        "inherit_from": "inheritFrom",
        "links": "links",
        "managed": "managed",
        "name": "name",
        "namespace": "namespace",
        "owner": "owner",
        "tags": "tags",
    }

    def __init__(
        self_,
        name: str,
        additional_owners: Union[List[EntityV3MetadataAdditionalOwnersItems], UnsetType] = unset,
        contacts: Union[List[EntityV3MetadataContactsItems], UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        inherit_from: Union[str, UnsetType] = unset,
        links: Union[List[EntityV3MetadataLinksItems], UnsetType] = unset,
        managed: Union[Dict[str, Any], UnsetType] = unset,
        namespace: Union[str, UnsetType] = unset,
        owner: Union[str, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of Entity V3 Metadata object.

        :param additional_owners: The additional owners of the entity, usually a team.
        :type additional_owners: [EntityV3MetadataAdditionalOwnersItems], optional

        :param contacts: A list of contacts for the entity.
        :type contacts: [EntityV3MetadataContactsItems], optional

        :param description: Short description of the entity. The UI can leverage the description for display.
        :type description: str, optional

        :param display_name: User friendly name of the entity. The UI can leverage the display name for display.
        :type display_name: str, optional

        :param id: A read-only globally unique identifier for the entity generated by Datadog.  User supplied values are ignored.
        :type id: str, optional

        :param inherit_from: The entity reference from which to inherit metadata
        :type inherit_from: str, optional

        :param links: A list of links for the entity.
        :type links: [EntityV3MetadataLinksItems], optional

        :param managed: A read-only set of Datadog managed attributes generated by Datadog.  User supplied values are ignored.
        :type managed: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param name: Unique name given to an entity under the kind/namespace.
        :type name: str

        :param namespace: Namespace is a part of unique identifier. It has a default value of 'default'.
        :type namespace: str, optional

        :param owner: The owner of the entity, usually a team.
        :type owner: str, optional

        :param tags: A set of custom tags.
        :type tags: [str], optional
        """
        if additional_owners is not unset:
            kwargs["additional_owners"] = additional_owners
        if contacts is not unset:
            kwargs["contacts"] = contacts
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if id is not unset:
            kwargs["id"] = id
        if inherit_from is not unset:
            kwargs["inherit_from"] = inherit_from
        if links is not unset:
            kwargs["links"] = links
        if managed is not unset:
            kwargs["managed"] = managed
        if namespace is not unset:
            kwargs["namespace"] = namespace
        if owner is not unset:
            kwargs["owner"] = owner
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.name = name
