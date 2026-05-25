# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


class AnalysisRequestRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "category": (str,),
            "checksum": (str,),
            "code": (str,),
            "entity_checked": (str, none_type),
            "id": (str,),
            "language": (str,),
            "regex": (str, none_type),
            "severity": (str,),
            "tree_sitter_query": (str,),
            "type": (str,),
        }

    attribute_map = {
        "category": "category",
        "checksum": "checksum",
        "code": "code",
        "entity_checked": "entity_checked",
        "id": "id",
        "language": "language",
        "regex": "regex",
        "severity": "severity",
        "tree_sitter_query": "tree_sitter_query",
        "type": "type",
    }

    def __init__(
        self_,
        category: str,
        checksum: str,
        code: str,
        id: str,
        language: str,
        severity: str,
        tree_sitter_query: str,
        type: str,
        entity_checked: Union[str, none_type, UnsetType] = unset,
        regex: Union[str, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        A static analysis rule to apply during code analysis.

        :param category: The category of the rule (for example, ``BEST_PRACTICES`` , ``SECURITY`` ).
        :type category: str

        :param checksum: A checksum of the rule definition.
        :type checksum: str

        :param code: The base64-encoded rule implementation code.
        :type code: str

        :param entity_checked: The code entity type checked by the rule, applicable when rule type is ``AST_CHECK``.
        :type entity_checked: str, none_type, optional

        :param id: The unique identifier of the rule.
        :type id: str

        :param language: The programming language this rule targets.
        :type language: str

        :param regex: A base64-encoded regex pattern used by the rule, applicable when rule type is ``REGEX``.
        :type regex: str, none_type, optional

        :param severity: The severity of findings from this rule (for example, ``ERROR`` , ``WARNING`` ).
        :type severity: str

        :param tree_sitter_query: The base64-encoded tree-sitter query used by the rule.
        :type tree_sitter_query: str

        :param type: The rule type indicating the detection mechanism (for example, ``TREE_SITTER_QUERY`` ).
        :type type: str
        """
        if entity_checked is not unset:
            kwargs["entity_checked"] = entity_checked
        if regex is not unset:
            kwargs["regex"] = regex
        super().__init__(kwargs)

        self_.category = category
        self_.checksum = checksum
        self_.code = code
        self_.id = id
        self_.language = language
        self_.severity = severity
        self_.tree_sitter_query = tree_sitter_query
        self_.type = type
