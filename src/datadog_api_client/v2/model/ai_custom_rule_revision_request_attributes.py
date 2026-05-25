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
    from datadog_api_client.v2.model.custom_rule_revision_attributes_category import (
        CustomRuleRevisionAttributesCategory,
    )
    from datadog_api_client.v2.model.ai_custom_rule_revision_execution_mode import AiCustomRuleRevisionExecutionMode
    from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import (
        CustomRuleRevisionAttributesSeverity,
    )


class AiCustomRuleRevisionRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.custom_rule_revision_attributes_category import (
            CustomRuleRevisionAttributesCategory,
        )
        from datadog_api_client.v2.model.ai_custom_rule_revision_execution_mode import AiCustomRuleRevisionExecutionMode
        from datadog_api_client.v2.model.custom_rule_revision_attributes_severity import (
            CustomRuleRevisionAttributesSeverity,
        )

        return {
            "category": (CustomRuleRevisionAttributesCategory,),
            "content": (str,),
            "cwe": (str, none_type),
            "description": (str,),
            "directories": ([str],),
            "execution_mode": (AiCustomRuleRevisionExecutionMode,),
            "globs": ([str],),
            "is_published": (bool,),
            "is_testing": (bool,),
            "severity": (CustomRuleRevisionAttributesSeverity,),
            "short_description": (str,),
            "version_id": (int,),
        }

    attribute_map = {
        "category": "category",
        "content": "content",
        "cwe": "cwe",
        "description": "description",
        "directories": "directories",
        "execution_mode": "execution_mode",
        "globs": "globs",
        "is_published": "is_published",
        "is_testing": "is_testing",
        "severity": "severity",
        "short_description": "short_description",
        "version_id": "version_id",
    }

    def __init__(
        self_,
        category: CustomRuleRevisionAttributesCategory,
        content: str,
        description: str,
        directories: List[str],
        execution_mode: AiCustomRuleRevisionExecutionMode,
        globs: List[str],
        is_published: bool,
        is_testing: bool,
        severity: CustomRuleRevisionAttributesSeverity,
        short_description: str,
        cwe: Union[str, none_type, UnsetType] = unset,
        version_id: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating an AI custom rule revision.

        :param category: Rule category
        :type category: CustomRuleRevisionAttributesCategory

        :param content: Base64-encoded AI model content for this revision.
        :type content: str

        :param cwe: The associated CWE identifier.
        :type cwe: str, none_type, optional

        :param description: Base64-encoded full description.
        :type description: str

        :param directories: Directory patterns this rule applies to.
        :type directories: [str]

        :param execution_mode: The execution mode for an AI rule revision.
        :type execution_mode: AiCustomRuleRevisionExecutionMode

        :param globs: File glob patterns this rule applies to.
        :type globs: [str]

        :param is_published: Whether this revision is published.
        :type is_published: bool

        :param is_testing: Whether this revision is for testing only.
        :type is_testing: bool

        :param severity: Rule severity
        :type severity: CustomRuleRevisionAttributesSeverity

        :param short_description: Base64-encoded short description.
        :type short_description: str

        :param version_id: The version identifier for this revision.
        :type version_id: int, optional
        """
        if cwe is not unset:
            kwargs["cwe"] = cwe
        if version_id is not unset:
            kwargs["version_id"] = version_id
        super().__init__(kwargs)

        self_.category = category
        self_.content = content
        self_.description = description
        self_.directories = directories
        self_.execution_mode = execution_mode
        self_.globs = globs
        self_.is_published = is_published
        self_.is_testing = is_testing
        self_.severity = severity
        self_.short_description = short_description
