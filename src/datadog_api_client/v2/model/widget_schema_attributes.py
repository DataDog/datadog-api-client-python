# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.definition import Definition


class WidgetSchemaAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.definition import Definition

        return {
            "created_at": (str,),
            "definition": (Definition,),
            "is_favorited": (bool,),
            "modified_at": (str,),
            "tags": ([str], none_type),
        }

    attribute_map = {
        "created_at": "created_at",
        "definition": "definition",
        "is_favorited": "is_favorited",
        "modified_at": "modified_at",
        "tags": "tags",
    }

    def __init__(
        self_,
        created_at: str,
        definition: Definition,
        is_favorited: bool,
        modified_at: str,
        tags: Union[List[str], none_type],
        **kwargs,
    ):
        """


        :param created_at: ISO 8601 timestamp of when the widget was created.
        :type created_at: str

        :param definition: The definition of a widget, including its type and configuration.
        :type definition: Definition

        :param is_favorited: Deprecated: this field is not functional and always returns False. **Deprecated**.
        :type is_favorited: bool

        :param modified_at: ISO 8601 timestamp of when the widget was last modified.
        :type modified_at: str

        :param tags: User-defined tags for organizing widgets.
        :type tags: [str], none_type
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.definition = definition
        self_.is_favorited = is_favorited
        self_.modified_at = modified_at
        self_.tags = tags
