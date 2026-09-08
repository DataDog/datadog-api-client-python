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
    from datadog_api_client.v2.model.argument import Argument
    from datadog_api_client.v2.model.custom_rule_revision_attributes_category import (
        CustomRuleRevisionAttributesCategory,
    )
    from datadog_api_client.v2.model.language import Language
    from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import (
        CustomRuleRevisionAttributesSeverity,
    )
    from datadog_api_client.v2.model.custom_rule_revision_test import CustomRuleRevisionTest


class CustomRuleRevisionInput(ModelNormal):
    @cached_property
    def additional_properties_type(_):
        return None

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.argument import Argument
        from datadog_api_client.v2.model.custom_rule_revision_attributes_category import (
            CustomRuleRevisionAttributesCategory,
        )
        from datadog_api_client.v2.model.language import Language
        from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import (
            CustomRuleRevisionAttributesSeverity,
        )
        from datadog_api_client.v2.model.custom_rule_revision_test import CustomRuleRevisionTest

        return {
            "arguments": ([Argument], none_type),
            "category": (CustomRuleRevisionAttributesCategory,),
            "checksum": (str,),
            "code": (str,),
            "created_at": (datetime,),
            "created_by": (str,),
            "creation_message": (str,),
            "cve": (str, none_type),
            "cwe": (str, none_type),
            "description": (str,),
            "documentation_url": (str, none_type),
            "id": (str,),
            "is_published": (bool,),
            "is_testing": (bool,),
            "language": (Language,),
            "severity": (CustomRuleRevisionAttributesSeverity,),
            "short_description": (str,),
            "should_use_ai_fix": (bool,),
            "tags": ([str], none_type),
            "tests": ([CustomRuleRevisionTest], none_type),
            "tree_sitter_query": (str,),
            "version_id": (int,),
        }

    attribute_map = {
        "arguments": "arguments",
        "category": "category",
        "checksum": "checksum",
        "code": "code",
        "created_at": "created_at",
        "created_by": "created_by",
        "creation_message": "creation_message",
        "cve": "cve",
        "cwe": "cwe",
        "description": "description",
        "documentation_url": "documentation_url",
        "id": "id",
        "is_published": "is_published",
        "is_testing": "is_testing",
        "language": "language",
        "severity": "severity",
        "short_description": "short_description",
        "should_use_ai_fix": "should_use_ai_fix",
        "tags": "tags",
        "tests": "tests",
        "tree_sitter_query": "tree_sitter_query",
        "version_id": "version_id",
    }
    read_only_vars = {
        "checksum",
        "created_at",
        "created_by",
        "id",
        "version_id",
    }

    def __init__(
        self_,
        arguments: Union[List[Argument], none_type, UnsetType] = unset,
        category: Union[CustomRuleRevisionAttributesCategory, UnsetType] = unset,
        checksum: Union[str, UnsetType] = unset,
        code: Union[str, UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        created_by: Union[str, UnsetType] = unset,
        creation_message: Union[str, UnsetType] = unset,
        cve: Union[str, none_type, UnsetType] = unset,
        cwe: Union[str, none_type, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        documentation_url: Union[str, none_type, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        is_published: Union[bool, UnsetType] = unset,
        is_testing: Union[bool, UnsetType] = unset,
        language: Union[Language, UnsetType] = unset,
        severity: Union[CustomRuleRevisionAttributesSeverity, UnsetType] = unset,
        short_description: Union[str, UnsetType] = unset,
        should_use_ai_fix: Union[bool, UnsetType] = unset,
        tags: Union[List[str], none_type, UnsetType] = unset,
        tests: Union[List[CustomRuleRevisionTest], none_type, UnsetType] = unset,
        tree_sitter_query: Union[str, UnsetType] = unset,
        version_id: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        A revision of a custom static analysis rule as embedded in a rule supplied by a create
        or update request. Nested revisions are sent flat, without a ``data`` / ``type`` / ``attributes``
        envelope. ``id`` , ``version_id`` , ``checksum`` , ``created_at`` and ``created_by`` are server-assigned
        and read-only; they are declared so that a ruleset previously read back can be supplied
        unchanged.

        :param arguments: Rule arguments
        :type arguments: [Argument], none_type, optional

        :param category: Rule category
        :type category: CustomRuleRevisionAttributesCategory, optional

        :param checksum: Code checksum
        :type checksum: str, optional

        :param code: Rule code
        :type code: str, optional

        :param created_at: Creation timestamp
        :type created_at: datetime, optional

        :param created_by: Creator identifier
        :type created_by: str, optional

        :param creation_message: Revision creation message
        :type creation_message: str, optional

        :param cve: Associated CVE
        :type cve: str, none_type, optional

        :param cwe: Associated CWE
        :type cwe: str, none_type, optional

        :param description: Base64-encoded full description
        :type description: str, optional

        :param documentation_url: Documentation URL
        :type documentation_url: str, none_type, optional

        :param id: Revision identifier
        :type id: str, optional

        :param is_published: Whether the revision should be published
        :type is_published: bool, optional

        :param is_testing: Whether this is a testing revision
        :type is_testing: bool, optional

        :param language: Programming language
        :type language: Language, optional

        :param severity: Rule severity
        :type severity: CustomRuleRevisionAttributesSeverity, optional

        :param short_description: Base64-encoded short description
        :type short_description: str, optional

        :param should_use_ai_fix: Whether to use AI for fixes
        :type should_use_ai_fix: bool, optional

        :param tags: Rule tags
        :type tags: [str], none_type, optional

        :param tests: Rule tests
        :type tests: [CustomRuleRevisionTest], none_type, optional

        :param tree_sitter_query: Tree-sitter query
        :type tree_sitter_query: str, optional

        :param version_id: Monotonically increasing version number of the revision.
        :type version_id: int, optional
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
        if creation_message is not unset:
            kwargs["creation_message"] = creation_message
        if cve is not unset:
            kwargs["cve"] = cve
        if cwe is not unset:
            kwargs["cwe"] = cwe
        if description is not unset:
            kwargs["description"] = description
        if documentation_url is not unset:
            kwargs["documentation_url"] = documentation_url
        if id is not unset:
            kwargs["id"] = id
        if is_published is not unset:
            kwargs["is_published"] = is_published
        if is_testing is not unset:
            kwargs["is_testing"] = is_testing
        if language is not unset:
            kwargs["language"] = language
        if severity is not unset:
            kwargs["severity"] = severity
        if short_description is not unset:
            kwargs["short_description"] = short_description
        if should_use_ai_fix is not unset:
            kwargs["should_use_ai_fix"] = should_use_ai_fix
        if tags is not unset:
            kwargs["tags"] = tags
        if tests is not unset:
            kwargs["tests"] = tests
        if tree_sitter_query is not unset:
            kwargs["tree_sitter_query"] = tree_sitter_query
        if version_id is not unset:
            kwargs["version_id"] = version_id
        super().__init__(kwargs)
