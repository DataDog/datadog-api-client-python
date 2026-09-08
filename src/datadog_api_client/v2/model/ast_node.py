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
    from datadog_api_client.v2.model.analysis_position import AnalysisPosition


class AstNode(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_position import AnalysisPosition

        return {
            "ast_type": (str,),
            "children": ([AstNode], none_type),
            "end": (AnalysisPosition,),
            "field_name": (str,),
            "start": (AnalysisPosition,),
        }

    attribute_map = {
        "ast_type": "ast_type",
        "children": "children",
        "end": "end",
        "field_name": "field_name",
        "start": "start",
    }

    def __init__(
        self_,
        ast_type: str,
        children: Union[List[AstNode], none_type],
        end: AnalysisPosition,
        start: AnalysisPosition,
        field_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A node in the abstract syntax tree of the parsed source code.

        :param ast_type: The tree-sitter node type of this AST node.
        :type ast_type: str

        :param children: The child nodes of this AST node, or null for a leaf node.
        :type children: [AstNode], none_type

        :param end: A position in source code, identified by line and column numbers.
        :type end: AnalysisPosition

        :param field_name: The name of the field this node occupies within its parent node, when the parent addresses it by name.
        :type field_name: str, optional

        :param start: A position in source code, identified by line and column numbers.
        :type start: AnalysisPosition
        """
        if field_name is not unset:
            kwargs["field_name"] = field_name
        super().__init__(kwargs)

        self_.ast_type = ast_type
        self_.children = children
        self_.end = end
        self_.start = start
