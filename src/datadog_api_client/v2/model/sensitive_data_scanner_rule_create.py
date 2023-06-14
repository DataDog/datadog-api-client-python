# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement
from datadog_api_client.v2.model.sensitive_data_scanner_rule_attributes import SensitiveDataScannerRuleAttributes
from datadog_api_client.v2.model.sensitive_data_scanner_text_replacement import SensitiveDataScannerTextReplacement

if TYPE_CHECKING:
    from datadog_api_client.v2.model.sensitive_data_scanner_rule_relationships import (
        SensitiveDataScannerRuleRelationships,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType


@dataclass
class SensitiveDataScannerRuleCreateJSON:
    description: Union[str, UnsetType] = unset
    excluded_namespaces: Union[List[str], UnsetType] = unset
    is_enabled: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    namespaces: Union[List[str], UnsetType] = unset
    pattern: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset
    text_replacement: Union[SensitiveDataScannerTextReplacement, UnsetType] = unset
    group: Union[str, UnsetType] = unset
    standard_pattern: Union[str, UnsetType] = unset


class SensitiveDataScannerRuleCreate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_rule_relationships import (
            SensitiveDataScannerRuleRelationships,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType

        return {
            "attributes": (SensitiveDataScannerRuleAttributes,),
            "relationships": (SensitiveDataScannerRuleRelationships,),
            "type": (SensitiveDataScannerRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "relationships": "relationships",
        "type": "type",
    }
    json_api_model = SensitiveDataScannerRuleCreateJSON

    def __init__(
        self_,
        attributes: SensitiveDataScannerRuleAttributes,
        relationships: SensitiveDataScannerRuleRelationships,
        type: SensitiveDataScannerRuleType,
        **kwargs,
    ):
        """
        Data related to the creation of a rule.

        :param attributes: Attributes of the Sensitive Data Scanner rule.
        :type attributes: SensitiveDataScannerRuleAttributes

        :param relationships: Relationships of a scanning rule.
        :type relationships: SensitiveDataScannerRuleRelationships

        :param type: Sensitive Data Scanner rule type.
        :type type: SensitiveDataScannerRuleType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.relationships = relationships
        self_.type = type
