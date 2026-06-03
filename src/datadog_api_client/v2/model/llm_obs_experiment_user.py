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


class LLMObsExperimentUser(ModelNormal):
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
        email: Union[str, UnsetType] = unset,
        handle: Union[str, UnsetType] = unset,
        icon: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        User data for the author of an experiment. Only present when ``include[user_data]`` is ``true``.

        :param email: Email address of the user.
        :type email: str, optional

        :param handle: Username or handle associated with the user's Datadog account.
        :type handle: str, optional

        :param icon: URL of the user's icon.
        :type icon: str, optional

        :param id: Unique identifier of the user.
        :type id: str, optional

        :param name: Display name of the user.
        :type name: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if handle is not unset:
            kwargs["handle"] = handle
        if icon is not unset:
            kwargs["icon"] = icon
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
