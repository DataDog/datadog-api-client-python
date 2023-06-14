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


class CIAppUserInfo(ModelNormal):
    _nullable = True

    @cached_property
    def openapi_types(_):
        return {
            "email": (str,),
            "name": (str,),
        }

    attribute_map = {
        "email": "email",
        "name": "name",
    }

    def __init__(self_, email: Union[str, UnsetType] = unset, name: Union[str, UnsetType] = unset, **kwargs):
        """
        Used to specify user-related information when the payload does not have Git information.
        For example, if Git information is missing for manually triggered pipelines, this field can be used instead.

        :param email: Email of the user.
        :type email: str, optional

        :param name: Name of the user.
        :type name: str, optional
        """
        if email is not unset:
            kwargs["email"] = email
        if name is not unset:
            kwargs["name"] = name
        super().__init__(kwargs)
