# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.definition import Definition


class CreateOrUpdateWidgetRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.definition import Definition

        return {
            "definition": (Definition,),
            "tags": ([str], none_type),
        }

    attribute_map = {
        "definition": "definition",
        "tags": "tags",
    }

    def __init__(self_, definition: Definition, tags: Union[List[str], none_type, UnsetType] = unset, **kwargs):
        """


        :param definition: The definition of a widget, including its type and configuration.
        :type definition: Definition

        :param tags: User-defined tags for organizing the widget.
        :type tags: [str], none_type, optional
        """
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.definition = definition
