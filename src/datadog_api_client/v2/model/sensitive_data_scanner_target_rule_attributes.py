# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelComposed,
    cached_property,
)


class SensitiveDataScannerTargetRuleAttributes(ModelComposed):
    def __init__(self, **kwargs):
        """
        Attributes of a rule of a scanning group of a target. They depend on the type of rule.

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

        :param pattern: Regular expression of the rule.
        :type pattern: str

        :param priority: Severity of the issues found by the rule.
        :type priority: SensitiveDataScannerRulePriority, optional

        :param rule_type: Type of a custom rule.
        :type rule_type: SensitiveDataScannerCustomRegexRuleType

        :param suppressions: Object describing suppressions for a rule, or the recommended suppression lists published by a standard pattern.
            There are three types of suppressions, `starts_with`, `ends_with`, and `exact_match`.
            Rules based on the Datadog library can use recommended or custom suppressions. Custom rules can only use custom suppressions.
            Suppressed matches are not obfuscated, counted in metrics, or displayed in the Findings page.
        :type suppressions: SensitiveDataScannerSuppressions, optional

        :param tags: List of tags.
        :type tags: [str], optional

        :param text_replacement: Object describing how the scanned event will be replaced.
        :type text_replacement: SensitiveDataScannerTextReplacement, optional
        """
        super().__init__(kwargs)

    @cached_property
    def _composed_schemas(_):
        # we need this here to make our import statements work
        # we must store _composed_schemas in here so the code is only run
        # when we invoke this method. If we kept this at the class
        # level we would get an error because the class level
        # code would be run when this module is imported, and these composed
        # classes don't exist yet because their module has not finished
        # loading
        from datadog_api_client.v2.model.sensitive_data_scanner_custom_regex_rule_attributes import (
            SensitiveDataScannerCustomRegexRuleAttributes,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_standard_regex_rule_attributes import (
            SensitiveDataScannerStandardRegexRuleAttributes,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_machine_learning_rule_attributes import (
            SensitiveDataScannerMachineLearningRuleAttributes,
        )

        return {
            "oneOf": [
                SensitiveDataScannerCustomRegexRuleAttributes,
                SensitiveDataScannerStandardRegexRuleAttributes,
                SensitiveDataScannerMachineLearningRuleAttributes,
            ],
        }
