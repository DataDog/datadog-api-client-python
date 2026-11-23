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
    from datadog_api_client.v2.model.sensitive_data_scanner_included_keyword_configuration import (
        SensitiveDataScannerIncludedKeywordConfiguration,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_rule_priority import SensitiveDataScannerRulePriority
    from datadog_api_client.v2.model.sensitive_data_scanner_standard_regex_rule_type import (
        SensitiveDataScannerStandardRegexRuleType,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_suppressions import SensitiveDataScannerSuppressions
    from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement


class SensitiveDataScannerStandardRegexRuleAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_included_keyword_configuration import (
            SensitiveDataScannerIncludedKeywordConfiguration,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_rule_priority import SensitiveDataScannerRulePriority
        from datadog_api_client.v2.model.sensitive_data_scanner_standard_regex_rule_type import (
            SensitiveDataScannerStandardRegexRuleType,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_suppressions import SensitiveDataScannerSuppressions
        from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import (
            SensitiveDataScannerTextReplacement,
        )

        return {
            "description": (str,),
            "excluded_namespaces": ([str],),
            "included_keyword_configuration": (SensitiveDataScannerIncludedKeywordConfiguration,),
            "is_enabled": (bool,),
            "name": (str,),
            "namespaces": ([str],),
            "priority": (SensitiveDataScannerRulePriority,),
            "rule_type": (SensitiveDataScannerStandardRegexRuleType,),
            "suppressions": (SensitiveDataScannerSuppressions,),
            "tags": ([str],),
            "text_replacement": (SensitiveDataScannerTextReplacement,),
        }

    attribute_map = {
        "description": "description",
        "excluded_namespaces": "excluded_namespaces",
        "included_keyword_configuration": "included_keyword_configuration",
        "is_enabled": "is_enabled",
        "name": "name",
        "namespaces": "namespaces",
        "priority": "priority",
        "rule_type": "rule_type",
        "suppressions": "suppressions",
        "tags": "tags",
        "text_replacement": "text_replacement",
    }

    def __init__(
        self_,
        rule_type: SensitiveDataScannerStandardRegexRuleType,
        description: Union[str, UnsetType] = unset,
        excluded_namespaces: Union[List[str], UnsetType] = unset,
        included_keyword_configuration: Union[SensitiveDataScannerIncludedKeywordConfiguration, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        namespaces: Union[List[str], UnsetType] = unset,
        priority: Union[SensitiveDataScannerRulePriority, UnsetType] = unset,
        suppressions: Union[SensitiveDataScannerSuppressions, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        text_replacement: Union[SensitiveDataScannerTextReplacement, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a rule based on a standard regex rule, whose pattern is maintained by Datadog.

        :param description: Description of the rule.
        :type description: str, optional

        :param excluded_namespaces: Attributes excluded from the scan. If namespaces is provided, it has to be a sub-path of the namespaces array.
        :type excluded_namespaces: [str], optional

        :param included_keyword_configuration: Object defining a set of keywords and a number of characters that help reduce noise.
            You can provide a list of keywords you would like to check within a defined proximity of the matching pattern.
            If any of the keywords are found within the proximity check, the match is kept.
            If none are found, the match is discarded.
        :type included_keyword_configuration: SensitiveDataScannerIncludedKeywordConfiguration, optional

        :param is_enabled: Whether or not the rule is enabled.
        :type is_enabled: bool, optional

        :param name: Name of the rule.
        :type name: str, optional

        :param namespaces: Attributes included in the scan. If namespaces is empty or missing, all attributes except excluded_namespaces are scanned.
            If both are missing the whole event is scanned.
        :type namespaces: [str], optional

        :param priority: Severity of the issues found by the rule.
        :type priority: SensitiveDataScannerRulePriority, optional

        :param rule_type: Type of a rule based on a standard regex rule.
        :type rule_type: SensitiveDataScannerStandardRegexRuleType

        :param suppressions: Object describing suppressions for a rule, or the recommended suppression lists published by a standard pattern.
            There are three types of suppressions, ``starts_with`` , ``ends_with`` , and ``exact_match``.
            Rules based on the Datadog library can use recommended or custom suppressions. Custom rules can only use custom suppressions.
            Suppressed matches are not obfuscated, counted in metrics, or displayed in the Findings page.
        :type suppressions: SensitiveDataScannerSuppressions, optional

        :param tags: List of tags.
        :type tags: [str], optional

        :param text_replacement: Object describing how the scanned event will be replaced.
        :type text_replacement: SensitiveDataScannerTextReplacement, optional
        """
        if description is not unset:
            kwargs["description"] = description
        if excluded_namespaces is not unset:
            kwargs["excluded_namespaces"] = excluded_namespaces
        if included_keyword_configuration is not unset:
            kwargs["included_keyword_configuration"] = included_keyword_configuration
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        if name is not unset:
            kwargs["name"] = name
        if namespaces is not unset:
            kwargs["namespaces"] = namespaces
        if priority is not unset:
            kwargs["priority"] = priority
        if suppressions is not unset:
            kwargs["suppressions"] = suppressions
        if tags is not unset:
            kwargs["tags"] = tags
        if text_replacement is not unset:
            kwargs["text_replacement"] = text_replacement
        super().__init__(kwargs)

        self_.rule_type = rule_type
