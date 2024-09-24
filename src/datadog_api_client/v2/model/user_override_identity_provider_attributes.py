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


class UserOverrideIdentityProviderAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "authentication_method": (str,),
        }

    attribute_map = {
        "authentication_method": "authentication_method",
    }

    def __init__(self_, authentication_method: Union[str, UnsetType] = unset, **kwargs):
        """
        The definition of ``UserOverrideIdentityProviderAttributes`` object.

        :param authentication_method: The ``UserOverrideIdentityProviderAttributes`` ``authentication_method``.
        :type authentication_method: str, optional
        """
        if authentication_method is not unset:
            kwargs["authentication_method"] = authentication_method
        super().__init__(kwargs)
