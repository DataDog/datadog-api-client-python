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
    from datadog_api_client.v2.model.change_event_attributes_author_type import ChangeEventAttributesAuthorType


class ChangeEventAttributesAuthor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_event_attributes_author_type import ChangeEventAttributesAuthorType

        return {
            "name": (str,),
            "type": (ChangeEventAttributesAuthorType,),
        }

    attribute_map = {
        "name": "name",
        "type": "type",
    }

    def __init__(
        self_,
        name: Union[str, UnsetType] = unset,
        type: Union[ChangeEventAttributesAuthorType, UnsetType] = unset,
        **kwargs,
    ):
        """
        The entity that made the change.

        :param name: The name of the user or system that made the change.
        :type name: str, optional

        :param type: The type of the author.
        :type type: ChangeEventAttributesAuthorType, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
