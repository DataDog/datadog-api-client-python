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


class AWSAuthConfigRole(ModelNormal):
    validations = {
        "role_name": {
            "max_length": 576,
            "min_length": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        return {
            "external_id": (str,),
            "role_name": (str,),
        }

    attribute_map = {
        "external_id": "external_id",
        "role_name": "role_name",
    }

    def __init__(self_, role_name: str, external_id: Union[str, UnsetType] = unset, **kwargs):
        """
        AWS Authentication config to integrate your account using an IAM role.

        :param external_id: AWS IAM External ID for associated role.
        :type external_id: str, optional

        :param role_name: AWS IAM Role name.
        :type role_name: str
        """
        if external_id is not unset:
            kwargs["external_id"] = external_id
        super().__init__(kwargs)

        self_.role_name = role_name
