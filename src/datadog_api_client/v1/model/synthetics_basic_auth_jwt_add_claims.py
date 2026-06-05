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


class SyntheticsBasicAuthJWTAddClaims(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "exp": (bool,),
            "iat": (bool,),
        }

    attribute_map = {
        "exp": "exp",
        "iat": "iat",
    }

    def __init__(self_, exp: Union[bool, UnsetType] = unset, iat: Union[bool, UnsetType] = unset, **kwargs):
        """
        Standard JWT claims to automatically inject.

        :param exp: Whether to inject the ``exp`` (expiration) claim.
        :type exp: bool, optional

        :param iat: Whether to inject the ``iat`` (issued at) claim.
        :type iat: bool, optional
        """
        if exp is not unset:
            kwargs["exp"] = exp
        if iat is not unset:
            kwargs["iat"] = iat
        super().__init__(kwargs)
