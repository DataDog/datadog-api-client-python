# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class IncidentTypeAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "description": (str,),
            "is_default": (bool,),
            "last_modified_by": (str,),
            "modified_at": (datetime,),
            "name": (str,),
            "prefix": (str,),
        }

    attribute_map = {
        "created_at": "createdAt",
        "created_by": "createdBy",
        "description": "description",
        "is_default": "is_default",
        "last_modified_by": "lastModifiedBy",
        "modified_at": "modifiedAt",
        "name": "name",
        "prefix": "prefix",
    }
    read_only_vars = {
        "created_at",
        "created_by",
        "last_modified_by",
        "modified_at",
        "prefix",
    }

    def __init__(
        self_,
        name: str,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        is_default: Union[bool, UnsetType] = unset,
        last_modified_by: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        prefix: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Incident type's attributes.

        :param created_at: Timestamp when the incident type was created.
        :type created_at: datetime, optional

        :param created_by: A unique identifier that represents the user that created the incident type.
        :type created_by: str, optional

        :param description: Text that describes the incident type.
        :type description: str, optional

        :param is_default: If true, this incident type will be used as the default incident type if a type is not specified during the creation of incident resources.
        :type is_default: bool, optional

        :param last_modified_by: A unique identifier that represents the user that last modified the incident type.
        :type last_modified_by: str, optional

        :param modified_at: Timestamp when the incident type was last modified.
        :type modified_at: datetime, optional

        :param name: The name of the incident type.
        :type name: str

        :param prefix: The string that will be prepended to the incident title across the Datadog app.
        :type prefix: str, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if description is not unset:
            kwargs["description"] = description
        if is_default is not unset:
            kwargs["is_default"] = is_default
        if last_modified_by is not unset:
            kwargs["last_modified_by"] = last_modified_by
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if prefix is not unset:
            kwargs["prefix"] = prefix
        super().__init__(kwargs)

        self_.name = name
