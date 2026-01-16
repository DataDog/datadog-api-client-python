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
    from datadog_api_client.v2.model.postmortem_cell_definition import PostmortemCellDefinition


class PostmortemCellAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_cell_definition import PostmortemCellDefinition

        return {
            "definition": (PostmortemCellDefinition,),
        }

    attribute_map = {
        "definition": "definition",
    }

    def __init__(self_, definition: Union[PostmortemCellDefinition, UnsetType] = unset, **kwargs):
        """
        Attributes of a postmortem cell

        :param definition: Definition of a postmortem cell
        :type definition: PostmortemCellDefinition, optional
        """
        if definition is not unset:
            kwargs["definition"] = definition
        super().__init__(kwargs)
