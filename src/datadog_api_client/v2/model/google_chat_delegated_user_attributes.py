# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class GoogleChatDelegatedUserAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "display_name": (str,),
            "email": (str,),
            "features": ([str],),
        }

    attribute_map = {
        "display_name": "display_name",
        "email": "email",
        "features": "features",
    }

    def __init__(
        self_,
        display_name: Union[str, UnsetType] = unset,
        email: Union[str, UnsetType] = unset,
        features: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Google Chat delegated user attributes.

        :param display_name: The delegated user's display name.
        :type display_name: str, optional

        :param email: The delegated user's email address.
        :type email: str, optional

        :param features: The list of features enabled for the delegated user.
        :type features: [str], optional
        """
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if email is not unset:
            kwargs["email"] = email
        if features is not unset:
            kwargs["features"] = features
        super().__init__(kwargs)
