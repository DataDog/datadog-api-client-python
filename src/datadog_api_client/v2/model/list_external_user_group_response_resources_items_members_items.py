# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class ListExternalUserGroupResponseResourcesItemsMembersItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_ref": (str,),
            "display": (str,),
            "type": (str,),
            "value": (str,),
        }

    attribute_map = {
        "_ref": "$ref",
        "display": "display",
        "type": "type",
        "value": "value",
    }

    def __init__(
        self_,
        _ref: Union[str, UnsetType] = unset,
        display: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        value: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of a member belonging to a group in the List SCIM groups response.

        :param _ref: The URI corresponding to a SCIM resource that is a member of this group.
        :type _ref: str, optional

        :param display: Full name of the user.
        :type display: str, optional

        :param type: A label indicating the type of resource. Only supported value is "User".
        :type type: str, optional

        :param value: The identifier of the member of this group.
        :type value: str, optional
        """
        if _ref is not unset:
            kwargs["_ref"] = _ref
        if display is not unset:
            kwargs["display"] = display
        if type is not unset:
            kwargs["type"] = type
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
