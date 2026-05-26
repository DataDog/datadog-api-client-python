# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.custom_rule_revision_attributes_category import (
        CustomRuleRevisionAttributesCategory,
    )
    from datadog_api_client.v2.model.ai_custom_rule_revision_execution_mode import AiCustomRuleRevisionExecutionMode
    from datadog_api_client.v2.model.language import Language
    from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import (
        CustomRuleRevisionAttributesSeverity,
    )


class AiPromptResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule_revision_attributes_category import (
            CustomRuleRevisionAttributesCategory,
        )
        from datadog_api_client.v2.model.ai_custom_rule_revision_execution_mode import AiCustomRuleRevisionExecutionMode
        from datadog_api_client.v2.model.language import Language
        from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import (
            CustomRuleRevisionAttributesSeverity,
        )

        return {
            "category": (CustomRuleRevisionAttributesCategory,),
            "checksum": (str,),
            "content": (str,),
            "cwe": (str,),
            "description": (str,),
            "directories": ([str],),
            "execution_mode": (AiCustomRuleRevisionExecutionMode,),
            "file_search_keywords": ([str],),
            "globs": ([str],),
            "is_default": (bool,),
            "is_testing": (bool,),
            "language": (Language,),
            "result_keywords_exclude": ([str],),
            "rule_version": (str,),
            "severity": (CustomRuleRevisionAttributesSeverity,),
            "short_description": (str,),
        }

    attribute_map = {
        "category": "category",
        "checksum": "checksum",
        "content": "content",
        "cwe": "cwe",
        "description": "description",
        "directories": "directories",
        "execution_mode": "execution_mode",
        "file_search_keywords": "file_search_keywords",
        "globs": "globs",
        "is_default": "is_default",
        "is_testing": "is_testing",
        "language": "language",
        "result_keywords_exclude": "result_keywords_exclude",
        "rule_version": "rule_version",
        "severity": "severity",
        "short_description": "short_description",
    }

    def __init__(
        self_,
        category: CustomRuleRevisionAttributesCategory,
        checksum: str,
        content: str,
        description: str,
        directories: List[str],
        execution_mode: AiCustomRuleRevisionExecutionMode,
        file_search_keywords: List[str],
        globs: List[str],
        is_default: bool,
        is_testing: bool,
        result_keywords_exclude: List[str],
        rule_version: str,
        severity: CustomRuleRevisionAttributesSeverity,
        short_description: str,
        cwe: Union[str, UnsetType] = unset,
        language: Union[Language, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response attributes of an AI prompt.

        :param category: Rule category
        :type category: CustomRuleRevisionAttributesCategory

        :param checksum: Checksum of the prompt content.
        :type checksum: str

        :param content: Base64-encoded AI prompt content.
        :type content: str

        :param cwe: The CWE identifier associated with this prompt.
        :type cwe: str, optional

        :param description: Base64-encoded full description.
        :type description: str

        :param directories: Directory patterns this prompt applies to.
        :type directories: [str]

        :param execution_mode: The execution mode for an AI rule revision.
        :type execution_mode: AiCustomRuleRevisionExecutionMode

        :param file_search_keywords: Keywords used to search for relevant files.
        :type file_search_keywords: [str]

        :param globs: File glob patterns this prompt applies to.
        :type globs: [str]

        :param is_default: Whether this is a default Datadog prompt.
        :type is_default: bool

        :param is_testing: Whether this prompt is for testing only.
        :type is_testing: bool

        :param language: Programming language
        :type language: Language, optional

        :param result_keywords_exclude: Keywords to exclude from results.
        :type result_keywords_exclude: [str]

        :param rule_version: The version of the rule this prompt is associated with.
        :type rule_version: str

        :param severity: Rule severity
        :type severity: CustomRuleRevisionAttributesSeverity

        :param short_description: Base64-encoded short description.
        :type short_description: str
        """
        if cwe is not unset:
            kwargs["cwe"] = cwe
        if language is not unset:
            kwargs["language"] = language
        super().__init__(kwargs)

        self_.category = category
        self_.checksum = checksum
        self_.content = content
        self_.description = description
        self_.directories = directories
        self_.execution_mode = execution_mode
        self_.file_search_keywords = file_search_keywords
        self_.globs = globs
        self_.is_default = is_default
        self_.is_testing = is_testing
        self_.result_keywords_exclude = result_keywords_exclude
        self_.rule_version = rule_version
        self_.severity = severity
        self_.short_description = short_description
