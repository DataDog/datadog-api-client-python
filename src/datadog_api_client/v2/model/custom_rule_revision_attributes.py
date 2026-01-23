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


class CustomRuleRevisionAttributes(ModelNormal):
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
            "arguments": ([Argument],),
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
            "is_published": (bool,),
            "is_testing": (bool,),
            "language": (Language,),
            "severity": (CustomRuleRevisionAttributesSeverity,),
            "short_description": (str,),
            "should_use_ai_fix": (bool,),
            "tags": ([str],),
            "tests": ([CustomRuleRevisionTest],),
            "tree_sitter_query": (str,),
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
        "is_published": "is_published",
        "is_testing": "is_testing",
        "language": "language",
        "severity": "severity",
        "short_description": "short_description",
        "should_use_ai_fix": "should_use_ai_fix",
        "tags": "tags",
        "tests": "tests",
        "tree_sitter_query": "tree_sitter_query",
    }

    def __init__(
        self_,
        arguments: List[Argument],
        category: CustomRuleRevisionAttributesCategory,
        checksum: str,
        code: str,
        created_at: datetime,
        created_by: str,
        creation_message: str,
        cve: Union[str, none_type],
        cwe: Union[str, none_type],
        description: str,
        documentation_url: Union[str, none_type],
        is_published: bool,
        is_testing: bool,
        language: Language,
        severity: CustomRuleRevisionAttributesSeverity,
        short_description: str,
        should_use_ai_fix: bool,
        tags: List[str],
        tests: List[CustomRuleRevisionTest],
        tree_sitter_query: str,
        **kwargs,
    ):
        """


        :param arguments: Rule arguments
        :type arguments: [Argument]

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

        :param cve: Associated CVE
        :type cve: str, none_type

        :param cwe: Associated CWE
        :type cwe: str, none_type

        :param description: Full description
        :type description: str

        :param documentation_url: Documentation URL
        :type documentation_url: str, none_type

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
        :type tags: [str]

        :param tests: Rule tests
        :type tests: [CustomRuleRevisionTest]

        :param tree_sitter_query: Tree-sitter query
        :type tree_sitter_query: str
        """
        super().__init__(kwargs)

        self_.arguments = arguments
        self_.category = category
        self_.checksum = checksum
        self_.code = code
        self_.created_at = created_at
        self_.created_by = created_by
        self_.creation_message = creation_message
        self_.cve = cve
        self_.cwe = cwe
        self_.description = description
        self_.documentation_url = documentation_url
        self_.is_published = is_published
        self_.is_testing = is_testing
        self_.language = language
        self_.severity = severity
        self_.short_description = short_description
        self_.should_use_ai_fix = should_use_ai_fix
        self_.tags = tags
        self_.tests = tests
        self_.tree_sitter_query = tree_sitter_query
