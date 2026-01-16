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
    from datadog_api_client.v2.model.postmortem_cell_attributes import PostmortemCellAttributes
    from datadog_api_client.v2.model.postmortem_cell_type import PostmortemCellType


class PostmortemCell(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.postmortem_cell_attributes import PostmortemCellAttributes
        from datadog_api_client.v2.model.postmortem_cell_type import PostmortemCellType

        return {
            "attributes": (PostmortemCellAttributes,),
            "id": (str,),
            "type": (PostmortemCellType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[PostmortemCellAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[PostmortemCellType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A cell in the postmortem

        :param attributes: Attributes of a postmortem cell
        :type attributes: PostmortemCellAttributes, optional

        :param id: The unique identifier of the cell
        :type id: str, optional

        :param type: The postmortem cell resource type.
        :type type: PostmortemCellType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
