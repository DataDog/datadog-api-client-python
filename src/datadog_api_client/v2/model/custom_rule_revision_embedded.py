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


class CustomRuleRevisionEmbedded(ModelNormal):
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
            "cve": (str,),
            "cwe": (str,),
            "description": (str,),
            "documentation_url": (str,),
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

    def __init__(
        self_,
        arguments: Union[List[Argument], none_type],
        category: CustomRuleRevisionAttributesCategory,
        checksum: str,
        code: str,
        created_at: datetime,
        created_by: str,
        creation_message: str,
        description: str,
        id: str,
        is_published: bool,
        is_testing: bool,
        language: Language,
        severity: CustomRuleRevisionAttributesSeverity,
        short_description: str,
        should_use_ai_fix: bool,
        tags: Union[List[str], none_type],
        tests: Union[List[CustomRuleRevisionTest], none_type],
        tree_sitter_query: str,
        version_id: int,
        cve: Union[str, UnsetType] = unset,
        cwe: Union[str, UnsetType] = unset,
        documentation_url: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A revision of a custom static analysis rule as embedded in a rule or ruleset response.

        :param arguments: Rule arguments
        :type arguments: [Argument], none_type

        :param category: Rule category
        :type category: CustomRuleRevisionAttributesCategory

        :param checksum: Code checksum
        :type checksum: str

        :param code: Rule code
        :type code: str

        :param created_at: Creation timestamp
        :type created_at: datetime

        :param created_by: Creator identifier
        :type created_by: str

        :param creation_message: Revision creation message
        :type creation_message: str

        :param cve: Associated CVE. Omitted when the revision has no associated CVE.
        :type cve: str, optional

        :param cwe: Associated CWE. Omitted when the revision has no associated CWE.
        :type cwe: str, optional

        :param description: Full description
        :type description: str

        :param documentation_url: Documentation URL. Omitted when the revision has no documentation URL.
        :type documentation_url: str, optional

        :param id: Revision identifier
        :type id: str

        :param is_published: Whether the revision is published
        :type is_published: bool

        :param is_testing: Whether this is a testing revision
        :type is_testing: bool

        :param language: Programming language
        :type language: Language

        :param severity: Rule severity
        :type severity: CustomRuleRevisionAttributesSeverity

        :param short_description: Short description
        :type short_description: str

        :param should_use_ai_fix: Whether to use AI for fixes
        :type should_use_ai_fix: bool

        :param tags: Rule tags
        :type tags: [str], none_type

        :param tests: Rule tests
        :type tests: [CustomRuleRevisionTest], none_type

        :param tree_sitter_query: Tree-sitter query
        :type tree_sitter_query: str

        :param version_id: Monotonically increasing version number of the revision.
        :type version_id: int
        """
        if cve is not unset:
            kwargs["cve"] = cve
        if cwe is not unset:
            kwargs["cwe"] = cwe
        if documentation_url is not unset:
            kwargs["documentation_url"] = documentation_url
        super().__init__(kwargs)

        self_.arguments = arguments
        self_.category = category
        self_.checksum = checksum
        self_.code = code
        self_.created_at = created_at
        self_.created_by = created_by
        self_.creation_message = creation_message
        self_.description = description
        self_.id = id
        self_.is_published = is_published
        self_.is_testing = is_testing
        self_.language = language
        self_.severity = severity
        self_.short_description = short_description
        self_.should_use_ai_fix = should_use_ai_fix
        self_.tags = tags
        self_.tests = tests
        self_.tree_sitter_query = tree_sitter_query
        self_.version_id = version_id
