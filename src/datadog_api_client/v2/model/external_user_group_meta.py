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


class ExternalUserGroupMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created": (datetime,),
            "last_modified": (datetime,),
            "location": (str,),
            "resource_type": (str,),
        }

    attribute_map = {
        "created": "created",
        "last_modified": "lastModified",
        "location": "location",
        "resource_type": "resourceType",
    }

    def __init__(
        self_,
        created: Union[datetime, UnsetType] = unset,
        last_modified: Union[datetime, UnsetType] = unset,
        location: Union[str, UnsetType] = unset,
        resource_type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Metadata associated with a SCIM group.

        :param created: The date and time the group was created.
        :type created: datetime, optional

        :param last_modified: The date and time the group was last changed.
        :type last_modified: datetime, optional

        :param location: URL identifying the resource.
        :type location: str, optional

        :param resource_type: Type of resource.
        :type resource_type: str, optional
        """
        if created is not unset:
            kwargs["created"] = created
        if last_modified is not unset:
            kwargs["last_modified"] = last_modified
        if location is not unset:
            kwargs["location"] = location
        if resource_type is not unset:
            kwargs["resource_type"] = resource_type
        super().__init__(kwargs)
