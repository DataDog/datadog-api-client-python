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


class GetCohortUsersResponseDataAttributesUsersItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "id": (str,),
            "name": (str,),
        }

    attribute_map = {
        "email": "email",
        "id": "id",
        "name": "name",
    }

    def __init__(
        self_,
        email: Union[str, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param email:
        :type email: str, optional

        :param id:
        :type id: str, optional

        :param name:
        :type name: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
