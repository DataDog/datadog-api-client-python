# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.model_lab_tag import ModelLabTag


class ModelLabProjectAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.model_lab_tag import ModelLabTag

        return {
            "artifact_storage_location": (str,),
            "created_at": (datetime,),
            "deleted_at": (datetime, none_type),
            "description": (str,),
            "external_url": (str, none_type),
            "is_starred": (bool,),
            "name": (str,),
            "owner_id": (str, none_type),
            "tags": ([ModelLabTag],),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "artifact_storage_location": "artifact_storage_location",
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "description": "description",
        "external_url": "external_url",
        "is_starred": "is_starred",
        "name": "name",
        "owner_id": "owner_id",
        "tags": "tags",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        artifact_storage_location: str,
        created_at: datetime,
        description: str,
        is_starred: bool,
        name: str,
        tags: List[ModelLabTag],
        updated_at: datetime,
        deleted_at: Union[datetime, none_type, UnsetType] = unset,
        external_url: Union[str, none_type, UnsetType] = unset,
        owner_id: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a Model Lab project.

        :param artifact_storage_location: The storage location for project artifacts.
        :type artifact_storage_location: str

        :param created_at: The date and time the project was created.
        :type created_at: datetime

        :param deleted_at: The date and time the project was soft-deleted.
        :type deleted_at: datetime, none_type, optional

        :param description: A description of the project.
        :type description: str

        :param external_url: An optional external URL associated with the project.
        :type external_url: str, none_type, optional

        :param is_starred: Whether the project is starred by the current user.
        :type is_starred: bool

        :param name: The name of the project.
        :type name: str

        :param owner_id: The UUID of the project owner.
        :type owner_id: str, none_type, optional

        :param tags: The list of tags associated with the project.
        :type tags: [ModelLabTag]

        :param updated_at: The date and time the project was last updated.
        :type updated_at: datetime
        """
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if external_url is not unset:
            kwargs["external_url"] = external_url
        if owner_id is not unset:
            kwargs["owner_id"] = owner_id
        super().__init__(kwargs)

        self_.artifact_storage_location = artifact_storage_location
        self_.created_at = created_at
        self_.description = description
        self_.is_starred = is_starred
        self_.name = name
        self_.tags = tags
        self_.updated_at = updated_at
