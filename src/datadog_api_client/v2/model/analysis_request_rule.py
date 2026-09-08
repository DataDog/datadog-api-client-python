# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.analysis_request_rule_argument import AnalysisRequestRuleArgument
    from datadog_api_client.v2.model.analysis_request_rule_test import AnalysisRequestRuleTest


class AnalysisRequestRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.analysis_request_rule_argument import AnalysisRequestRuleArgument
        from datadog_api_client.v2.model.analysis_request_rule_test import AnalysisRequestRuleTest

        return {
            "arguments": ([AnalysisRequestRuleArgument],),
            "category": (str,),
            "checksum": (str,),
            "code": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "cve": (str,),
            "cwe": (str,),
            "description": (str,),
            "documentation_url": (str,),
            "entity_checked": (str, none_type),
            "id": (str,),
            "is_published": (bool,),
            "is_testing": (bool,),
            "language": (str,),
            "last_updated_at": (datetime,),
            "last_updated_by": (str,),
            "name": (str,),
            "regex": (str, none_type),
            "severity": (str,),
            "short_description": (str,),
            "should_use_ai_fix": (bool,),
            "tests": ([AnalysisRequestRuleTest],),
            "tree_sitter_query": (str,),
            "type": (str,),
        }

    attribute_map = {
        "arguments": "arguments",
        "category": "category",
        "checksum": "checksum",
        "code": "code",
        "created_at": "created_at",
        "created_by": "created_by",
        "cve": "cve",
        "cwe": "cwe",
        "description": "description",
        "documentation_url": "documentation_url",
        "entity_checked": "entity_checked",
        "id": "id",
        "is_published": "is_published",
        "is_testing": "is_testing",
        "language": "language",
        "last_updated_at": "last_updated_at",
        "last_updated_by": "last_updated_by",
        "name": "name",
        "regex": "regex",
        "severity": "severity",
        "short_description": "short_description",
        "should_use_ai_fix": "should_use_ai_fix",
        "tests": "tests",
        "tree_sitter_query": "tree_sitter_query",
        "type": "type",
    }
    read_only_vars = {
        "created_at",
        "created_by",
        "last_updated_at",
        "last_updated_by",
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
        arguments: Union[List[AnalysisRequestRuleArgument], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        cve: Union[str, UnsetType] = unset,
        cwe: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        documentation_url: Union[str, UnsetType] = unset,
        entity_checked: Union[str, none_type, UnsetType] = unset,
        is_published: Union[bool, UnsetType] = unset,
        is_testing: Union[bool, UnsetType] = unset,
        last_updated_at: Union[datetime, UnsetType] = unset,
        last_updated_by: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        regex: Union[str, none_type, UnsetType] = unset,
        short_description: Union[str, UnsetType] = unset,
        should_use_ai_fix: Union[bool, UnsetType] = unset,
        tests: Union[List[AnalysisRequestRuleTest], UnsetType] = unset,
        **kwargs,
    ):
        """
        A static analysis rule to apply during code analysis. Clients forward complete rule
        objects returned by the rulesets endpoints, so every member of that resource is
        declared here; only ``id`` , ``category`` , ``checksum`` , ``language`` , ``severity`` ,
        ``tree_sitter_query`` , ``entity_checked`` , ``regex`` , ``type`` and ``code`` are read by this
        operation and the rest are ignored. The schema stays open so that any member beyond
        the forwarded rule resource is reported as a promotion candidate rather than
        rejected; it can be closed once that telemetry confirms none remain.

        :param arguments: The configurable arguments accepted by the rule. Forwarded from the rulesets endpoints; ignored by this operation.
        :type arguments: [AnalysisRequestRuleArgument], optional

        :param category: The category of the rule (for example, ``BEST_PRACTICES`` , ``SECURITY`` ).
        :type category: str

        :param checksum: A checksum of the rule definition.
        :type checksum: str

        :param code: The base64-encoded rule implementation code.
        :type code: str

        :param created_at: The date and time when the rule was created. Server-assigned by the rulesets endpoints; ignored by this operation.
        :type created_at: datetime, optional

        :param created_by: The identifier of the user or system that created the rule. Server-assigned by the rulesets endpoints; ignored by this operation.
        :type created_by: str, optional

        :param cve: The CVE identifier associated with the rule. Forwarded from the rulesets endpoints; ignored by this operation.
        :type cve: str, optional

        :param cwe: The CWE identifier associated with the rule. Forwarded from the rulesets endpoints; ignored by this operation.
        :type cwe: str, optional

        :param description: A detailed explanation of what the rule detects. Forwarded from the rulesets endpoints; ignored by this operation.
        :type description: str, optional

        :param documentation_url: A URL pointing to the rule documentation. Forwarded from the rulesets endpoints; ignored by this operation.
        :type documentation_url: str, optional

        :param entity_checked: The code entity type checked by the rule, applicable when rule type is ``AST_CHECK``.
        :type entity_checked: str, none_type, optional

        :param id: The unique identifier of the rule.
        :type id: str

        :param is_published: Whether the rule is published. Forwarded from the rulesets endpoints; ignored by this operation.
        :type is_published: bool, optional

        :param is_testing: Whether the rule is in testing mode. Forwarded from the rulesets endpoints; ignored by this operation.
        :type is_testing: bool, optional

        :param language: The programming language this rule targets.
        :type language: str

        :param last_updated_at: The date and time when the rule was last modified. Server-assigned by the rulesets endpoints; ignored by this operation.
        :type last_updated_at: datetime, optional

        :param last_updated_by: The identifier of the user or system that last updated the rule. Server-assigned by the rulesets endpoints; ignored by this operation.
        :type last_updated_by: str, optional

        :param name: The name of the rule. Forwarded from the rulesets endpoints; ignored by this operation.
        :type name: str, optional

        :param regex: A base64-encoded regex pattern used by the rule, applicable when rule type is ``REGEX``.
        :type regex: str, none_type, optional

        :param severity: The severity of findings from this rule (for example, ``ERROR`` , ``WARNING`` ).
        :type severity: str

        :param short_description: A brief summary of what the rule detects. Forwarded from the rulesets endpoints; ignored by this operation.
        :type short_description: str, optional

        :param should_use_ai_fix: Whether an AI-generated fix should be offered. Forwarded from the rulesets endpoints; ignored by this operation.
        :type should_use_ai_fix: bool, optional

        :param tests: The test cases associated with the rule. Forwarded from the rulesets endpoints; ignored by this operation.
        :type tests: [AnalysisRequestRuleTest], optional

        :param tree_sitter_query: The base64-encoded tree-sitter query used by the rule.
        :type tree_sitter_query: str

        :param type: The rule type indicating the detection mechanism (for example, ``TREE_SITTER_QUERY`` ).
        :type type: str
        """
        if arguments is not unset:
            kwargs["arguments"] = arguments
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if created_by is not unset:
            kwargs["created_by"] = created_by
        if cve is not unset:
            kwargs["cve"] = cve
        if cwe is not unset:
            kwargs["cwe"] = cwe
        if description is not unset:
            kwargs["description"] = description
        if documentation_url is not unset:
            kwargs["documentation_url"] = documentation_url
        if entity_checked is not unset:
            kwargs["entity_checked"] = entity_checked
        if is_published is not unset:
            kwargs["is_published"] = is_published
        if is_testing is not unset:
            kwargs["is_testing"] = is_testing
        if last_updated_at is not unset:
            kwargs["last_updated_at"] = last_updated_at
        if last_updated_by is not unset:
            kwargs["last_updated_by"] = last_updated_by
        if name is not unset:
            kwargs["name"] = name
        if regex is not unset:
            kwargs["regex"] = regex
        if short_description is not unset:
            kwargs["short_description"] = short_description
        if should_use_ai_fix is not unset:
            kwargs["should_use_ai_fix"] = should_use_ai_fix
        if tests is not unset:
            kwargs["tests"] = tests
        super().__init__(kwargs)

        self_.category = category
        self_.checksum = checksum
        self_.code = code
        self_.id = id
        self_.language = language
        self_.severity = severity
        self_.tree_sitter_query = tree_sitter_query
        self_.type = type
