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


class HTTPHeaderUpdate(ModelNormal):
    validations = {
        "name": {},
    }

    @cached_property
    def openapi_types(_):
        return {
            "deleted": (bool,),
            "name": (str,),
            "value": (str,),
        }

    attribute_map = {
        "deleted": "deleted",
        "name": "name",
        "value": "value",
    }

    def __init__(
        self_, name: str, deleted: Union[bool, UnsetType] = unset, value: Union[str, UnsetType] = unset, **kwargs
    ):
        """
        The definition of ``HTTPHeaderUpdate`` object.

        :param deleted: Should the header be deleted.
        :type deleted: bool, optional

        :param name: The ``HTTPHeaderUpdate`` ``name``.
        :type name: str

        :param value: The ``HTTPHeaderUpdate`` ``value``.
        :type value: str, optional
        """
        if deleted is not unset:
            kwargs["deleted"] = deleted
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)

        self_.name = name
