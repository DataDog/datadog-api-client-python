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


class SyntheticsApiMultistepSubtestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "public_id": (str,),
        }

    attribute_map = {
        "name": "name",
        "public_id": "public_id",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, public_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Attributes of a Synthetic API multistep subtest.

        :param name: Name of the subtest.
        :type name: str, optional

        :param public_id: The public ID of the subtest.
        :type public_id: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if public_id is not unset:
            kwargs["public_id"] = public_id
        super().__init__(kwargs)
