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
    from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items_data import (
        GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsData,
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
        from datadog_api_client.v2.model.get_multiple_rulesets_response_data_attributes_rulesets_items_rules_items_data import (
            GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsData,
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
            "data": (GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsData,),
            "description": (str,),
            "documentation_url": (str,),
            "entity_checked": (str,),
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
        "data": "data",
        "description": "description",
        "documentation_url": "documentation_url",
        "entity_checked": "entity_checked",
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
        data: GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsData,
        arguments: Union[
            List[GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsArgumentsItems], UnsetType
        ] = unset,
        category: Union[str, UnsetType] = unset,
        checksum: Union[str, UnsetType] = unset,
        code: Union[str, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        cve: Union[str, UnsetType] = unset,
        cwe: Union[str, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        documentation_url: Union[str, UnsetType] = unset,
        entity_checked: Union[str, UnsetType] = unset,
        is_published: Union[bool, UnsetType] = unset,
        is_testing: Union[bool, UnsetType] = unset,
        language: Union[str, UnsetType] = unset,
        last_updated_at: Union[datetime, UnsetType] = unset,
        last_updated_by: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        regex: Union[str, UnsetType] = unset,
        severity: Union[str, UnsetType] = unset,
        short_description: Union[str, UnsetType] = unset,
        should_use_ai_fix: Union[bool, UnsetType] = unset,
        tests: Union[
            List[GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsTestsItems], UnsetType
        ] = unset,
        tree_sitter_query: Union[str, UnsetType] = unset,
        type: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A static analysis rule within a ruleset, including its definition, metadata, and associated test cases.

        :param arguments: The list of configurable arguments accepted by this rule.
        :type arguments: [GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsArgumentsItems], optional

        :param category: The category classifying the type of issue this rule detects (e.g., security, style, performance).
        :type category: str, optional

        :param checksum: A checksum of the rule definition used to detect changes.
        :type checksum: str, optional

        :param code: The rule implementation code used by the static analysis engine.
        :type code: str, optional

        :param created_at: The date and time when the rule was created.
        :type created_at: datetime, optional

        :param created_by: The identifier of the user or system that created the rule.
        :type created_by: str, optional

        :param cve: The CVE identifier associated with the vulnerability this rule detects, if applicable.
        :type cve: str, optional

        :param cwe: The CWE identifier associated with the weakness category this rule detects, if applicable.
        :type cwe: str, optional

        :param data: The resource identifier and type for a static analysis rule.
        :type data: GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsData

        :param description: A detailed explanation of what the rule detects and why it matters.
        :type description: str, optional

        :param documentation_url: A URL pointing to additional documentation for this rule.
        :type documentation_url: str, optional

        :param entity_checked: The code entity type (e.g., function, class, variable) that this rule inspects.
        :type entity_checked: str, optional

        :param is_published: Indicates whether the rule is publicly published and available to all users.
        :type is_published: bool, optional

        :param is_testing: Indicates whether the rule is in testing mode and not yet promoted to production.
        :type is_testing: bool, optional

        :param language: The programming language this rule applies to.
        :type language: str, optional

        :param last_updated_at: The date and time when the rule was last modified.
        :type last_updated_at: datetime, optional

        :param last_updated_by: The identifier of the user or system that last updated the rule.
        :type last_updated_by: str, optional

        :param name: The unique name identifying this rule within its ruleset.
        :type name: str, optional

        :param regex: A regular expression pattern used by the rule for pattern-based detection.
        :type regex: str, optional

        :param severity: The severity level of findings produced by this rule (e.g., ERROR, WARNING, NOTICE).
        :type severity: str, optional

        :param short_description: A brief summary of what the rule detects, suitable for display in listings.
        :type short_description: str, optional

        :param should_use_ai_fix: Indicates whether an AI-generated fix suggestion should be offered for findings from this rule.
        :type should_use_ai_fix: bool, optional

        :param tests: The list of test cases used to validate the rule's behavior.
        :type tests: [GetMultipleRulesetsResponseDataAttributesRulesetsItemsRulesItemsTestsItems], optional

        :param tree_sitter_query: The Tree-sitter query expression used by the rule to match code patterns in the AST.
        :type tree_sitter_query: str, optional

        :param type: The rule type indicating the detection mechanism used (e.g., tree_sitter, regex).
        :type type: str, optional
        """
        if arguments is not unset:
            kwargs["arguments"] = arguments
        if category is not unset:
            kwargs["category"] = category
        if checksum is not unset:
            kwargs["checksum"] = checksum
        if code is not unset:
            kwargs["code"] = code
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
        if language is not unset:
            kwargs["language"] = language
        if last_updated_at is not unset:
            kwargs["last_updated_at"] = last_updated_at
        if last_updated_by is not unset:
            kwargs["last_updated_by"] = last_updated_by
        if name is not unset:
            kwargs["name"] = name
        if regex is not unset:
            kwargs["regex"] = regex
        if severity is not unset:
            kwargs["severity"] = severity
        if short_description is not unset:
            kwargs["short_description"] = short_description
        if should_use_ai_fix is not unset:
            kwargs["should_use_ai_fix"] = should_use_ai_fix
        if tests is not unset:
            kwargs["tests"] = tests
        if tree_sitter_query is not unset:
            kwargs["tree_sitter_query"] = tree_sitter_query
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)

        self_.data = data
