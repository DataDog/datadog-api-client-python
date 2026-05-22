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


class LLMObsDatasetDraftStateUser(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "handle": (str,),
            "icon": (str,),
            "id": (str,),
            "name": (str,),
        }

    attribute_map = {
        "email": "email",
        "handle": "handle",
        "icon": "icon",
        "id": "id",
        "name": "name",
    }

    def __init__(
        self_,
        id: str,
        email: Union[str, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        icon: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        User information associated with a dataset draft state.

        :param email: Email address of the user.
        :type email: str, optional

        :param handle: Handle of the user.
        :type handle: str, optional

        :param icon: Icon for the user.
        :type icon: str, optional

        :param id: Unique identifier of the user holding the draft lock.
        :type id: str

        :param name: Display name of the user.
        :type name: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if handle is not unset:
            kwargs["handle"] = handle
        if icon is not unset:
            kwargs["icon"] = icon
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)

        self_.id = id
