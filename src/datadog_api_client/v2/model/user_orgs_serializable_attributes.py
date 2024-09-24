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


class UserOrgsSerializableAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "disabled": (bool,),
            "email": (str,),
            "name": (str,),
            "org_id": (str,),
            "title": (str,),
            "verified": (bool,),
        }

    attribute_map = {
        "disabled": "disabled",
        "email": "email",
        "name": "name",
        "org_id": "org_id",
        "title": "title",
        "verified": "verified",
    }

    def __init__(
        self_,
        disabled: Union[bool, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        org_id: Union[str, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        verified: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UserOrgsSerializableAttributes`` object.

        :param disabled: The ``UserOrgsSerializableAttributes`` ``disabled``.
        :type disabled: bool, optional

        :param email: The ``UserOrgsSerializableAttributes`` ``email``.
        :type email: str, optional

        :param name: The ``UserOrgsSerializableAttributes`` ``name``.
        :type name: str, optional

        :param org_id: The ``UserOrgsSerializableAttributes`` ``org_id``.
        :type org_id: str, optional

        :param title: The ``UserOrgsSerializableAttributes`` ``title``.
        :type title: str, optional

        :param verified: The ``UserOrgsSerializableAttributes`` ``verified``.
        :type verified: bool, optional
        """
        if disabled is not unset:
            kwargs["disabled"] = disabled
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        if org_id is not unset:
            kwargs["org_id"] = org_id
        if title is not unset:
            kwargs["title"] = title
        if verified is not unset:
            kwargs["verified"] = verified
        super().__init__(kwargs)
