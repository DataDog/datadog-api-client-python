# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items_arguments_items import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsArgumentsItems,
    )
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items_tests_items import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsTestsItems,
    )


class GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items_arguments_items import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsArgumentsItems,
        )
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items_tests_items import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsTestsItems,
        )

        return {
            "arguments": ([GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsArgumentsItems],),
            "category": (str,),
            "checksum": (str,),
            "code": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "cve": (str,),
            "cwe": (str,),
            "description": (str,),
            "documentation_url": (str,),
            "entity_checked": (str,),
            "id": (str,),
            "is_published": (bool,),
            "is_testing": (bool,),
            "language": (str,),
            "last_updated_at": (datetime,),
            "last_updated_by": (str,),
            "name": (str,),
            "regex": (str,),
            "severity": (str,),
            "short_description": (str,),
            "should_use_ai_fix": (bool,),
            "tests": ([GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsTestsItems],),
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

    def __init__(
        self_,
        arguments: List[GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsArgumentsItems],
        category: str,
        checksum: str,
        code: str,
        created_at: datetime,
        created_by: str,
        description: str,
        id: str,
        is_published: bool,
        is_testing: bool,
        language: str,
        last_updated_at: datetime,
        last_updated_by: str,
        name: str,
        severity: str,
        short_description: str,
        should_use_ai_fix: bool,
        tests: List[GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsTestsItems],
        type: str,
        cve: Union[str, UnsetType] = unset,
        cwe: Union[str, UnsetType] = unset,
        documentation_url: Union[str, UnsetType] = unset,
        entity_checked: Union[str, UnsetType] = unset,
        regex: Union[str, UnsetType] = unset,
        tree_sitter_query: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A static analysis rule within a ruleset, including its definition, metadata, and associated test cases.

        :param arguments: The list of configurable arguments accepted by this rule.
        :type arguments: [GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsArgumentsItems]

        :param category: The category classifying the type of issue this rule detects (e.g., security, style, performance).
        :type category: str

        :param checksum: A checksum of the rule definition used to detect changes.
        :type checksum: str

        :param code: The rule implementation code used by the static analysis engine.
        :type code: str

        :param created_at: The date and time when the rule was created.
        :type created_at: datetime

        :param created_by: The identifier of the user or system that created the rule.
        :type created_by: str

        :param cve: The CVE identifier associated with the vulnerability this rule detects, if applicable.
        :type cve: str, optional

        :param cwe: The CWE identifier associated with the weakness category this rule detects, if applicable.
        :type cwe: str, optional

        :param description: A detailed explanation of what the rule detects and why it matters.
        :type description: str

        :param documentation_url: A URL pointing to additional documentation for this rule.
        :type documentation_url: str, optional

        :param entity_checked: The code entity type (e.g., function, class, variable) that this rule inspects.
        :type entity_checked: str, optional

        :param id: The unique identifier of the rule, which is the same as its name.
        :type id: str

        :param is_published: Indicates whether the rule is publicly published and available to all users.
        :type is_published: bool

        :param is_testing: Indicates whether the rule is in testing mode and not yet promoted to production.
        :type is_testing: bool

        :param language: The programming language this rule applies to.
        :type language: str

        :param last_updated_at: The date and time when the rule was last modified.
        :type last_updated_at: datetime

        :param last_updated_by: The identifier of the user or system that last updated the rule.
        :type last_updated_by: str

        :param name: The unique name identifying this rule within its ruleset.
        :type name: str

        :param regex: A regular expression pattern used by the rule for pattern-based detection.
        :type regex: str, optional

        :param severity: The severity level of findings produced by this rule (e.g., ERROR, WARNING, NOTICE).
        :type severity: str

        :param short_description: A brief summary of what the rule detects, suitable for display in listings.
        :type short_description: str

        :param should_use_ai_fix: Indicates whether an AI-generated fix suggestion should be offered for findings from this rule.
        :type should_use_ai_fix: bool

        :param tests: The list of test cases used to validate the rule's behavior.
        :type tests: [GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsTestsItems]

        :param tree_sitter_query: The Tree-sitter query expression used by the rule to match code patterns in the AST.
        :type tree_sitter_query: str, optional

        :param type: The rule type indicating the detection mechanism used (e.g., tree_sitter, regex).
        :type type: str
        """
        if cve is not unset:
            kwargs["cve"] = cve
        if cwe is not unset:
            kwargs["cwe"] = cwe
        if documentation_url is not unset:
            kwargs["documentation_url"] = documentation_url
        if entity_checked is not unset:
            kwargs["entity_checked"] = entity_checked
        if regex is not unset:
            kwargs["regex"] = regex
        if tree_sitter_query is not unset:
            kwargs["tree_sitter_query"] = tree_sitter_query
        super().__init__(kwargs)

        self_.arguments = arguments
        self_.category = category
        self_.checksum = checksum
        self_.code = code
        self_.created_at = created_at
        self_.created_by = created_by
        self_.description = description
        self_.id = id
        self_.is_published = is_published
        self_.is_testing = is_testing
        self_.language = language
        self_.last_updated_at = last_updated_at
        self_.last_updated_by = last_updated_by
        self_.name = name
        self_.severity = severity
        self_.short_description = short_description
        self_.should_use_ai_fix = should_use_ai_fix
        self_.tests = tests
        self_.type = type
