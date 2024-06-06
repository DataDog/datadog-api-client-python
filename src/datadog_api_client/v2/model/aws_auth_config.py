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


class AWSAuthConfig(ModelNormal):
    validations = {
        "access_key_id": {
            "max_length": 128,
            "min_length": 16,
        },
        "external_id": {},
        "role_name": {
            "max_length": 576,
            "min_length": 1,
        },
        "secret_access_key": {
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "access_key_id": (str,),
            "external_id": (str,),
            "role_name": (str,),
            "secret_access_key": (str,),
        }

    attribute_map = {
        "access_key_id": "access_key_id",
        "external_id": "external_id",
        "role_name": "role_name",
        "secret_access_key": "secret_access_key",
    }

    def __init__(
        self_,
        access_key_id: Union[str, UnsetType] = unset,
        external_id: Union[str, UnsetType] = unset,
        role_name: Union[str, UnsetType] = unset,
        secret_access_key: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Authentication config

        :param access_key_id: AWS Access Key ID
        :type access_key_id: str, optional

        :param external_id: AWS IAM External ID for associated role
        :type external_id: str, optional

        :param role_name: AWS IAM Role name
        :type role_name: str, optional

        :param secret_access_key: AWS Secret Access Key
        :type secret_access_key: str, optional
        """
        if access_key_id is not unset:
            kwargs["access_key_id"] = access_key_id
        if external_id is not unset:
            kwargs["external_id"] = external_id
        if role_name is not unset:
            kwargs["role_name"] = role_name
        if secret_access_key is not unset:
            kwargs["secret_access_key"] = secret_access_key
        super().__init__(kwargs)
