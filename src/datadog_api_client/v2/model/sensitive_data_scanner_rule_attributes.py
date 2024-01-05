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
    from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement


class SensitiveDataScannerRuleAttributes(ModelNormal):
    validations = {
        "priority": {
            "inclusive_maximum": 5,
            "inclusive_minimum": 1,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_included_keyword_configuration import (
            SensitiveDataScannerIncludedKeywordConfiguration,
        )
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
            "pattern": (str,),
            "priority": (int,),
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
        "pattern": "pattern",
        "priority": "priority",
        "tags": "tags",
        "text_replacement": "text_replacement",
    }

    def __init__(
        self_,
        description: Union[str, UnsetType] = unset,
        excluded_namespaces: Union[List[str], UnsetType] = unset,
        included_keyword_configuration: Union[SensitiveDataScannerIncludedKeywordConfiguration, UnsetType] = unset,
        is_enabled: Union[bool, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        namespaces: Union[List[str], UnsetType] = unset,
        pattern: Union[str, UnsetType] = unset,
        priority: Union[int, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        text_replacement: Union[SensitiveDataScannerTextReplacement, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of the Sensitive Data Scanner rule.

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

        :param pattern: Not included if there is a relationship to a standard pattern.
        :type pattern: str, optional

        :param priority: Integer from 1 (high) to 5 (low) indicating rule issue severity.
        :type priority: int, optional

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
        if pattern is not unset:
            kwargs["pattern"] = pattern
        if priority is not unset:
            kwargs["priority"] = priority
        if tags is not unset:
            kwargs["tags"] = tags
        if text_replacement is not unset:
            kwargs["text_replacement"] = text_replacement
        super().__init__(kwargs)
