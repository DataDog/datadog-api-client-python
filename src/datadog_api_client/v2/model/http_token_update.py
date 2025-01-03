# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.token_type import TokenType


class HTTPTokenUpdate(ModelNormal):
    validations = {
        "name": {},
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.token_type import TokenType

        return {
            "deleted": (bool,),
            "name": (str,),
            "type": (TokenType,),
            "value": (str,),
        }

    attribute_map = {
        "deleted": "deleted",
        "name": "name",
        "type": "type",
        "value": "value",
    }

    def __init__(self_, name: str, type: TokenType, value: str, deleted: Union[bool, UnsetType] = unset, **kwargs):
        """
        The definition of ``HTTPTokenUpdate`` object.

        :param deleted: Should the header be deleted.
        :type deleted: bool, optional

        :param name: The ``HTTPToken`` ``name``.
        :type name: str

        :param type: The definition of ``TokenType`` object.
        :type type: TokenType

        :param value: The ``HTTPToken`` ``value``.
        :type value: str
        """
        if deleted is not unset:
            kwargs["deleted"] = deleted
        super().__init__(kwargs)

        self_.name = name
        self_.type = type
        self_.value = value
