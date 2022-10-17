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
class SensitiveDataScannerRuleResponseJSON:
    id: str
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


class SensitiveDataScannerRuleResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_rule_relationships import (
            SensitiveDataScannerRuleRelationships,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType

        return {
            "attributes": (SensitiveDataScannerRuleAttributes,),
            "id": (str,),
            "relationships": (SensitiveDataScannerRuleRelationships,),
            "type": (SensitiveDataScannerRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }
    json_api_model = SensitiveDataScannerRuleResponseJSON

    def __init__(
        self_,
        attributes: Union[SensitiveDataScannerRuleAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[SensitiveDataScannerRuleRelationships, UnsetType] = unset,
        type: Union[SensitiveDataScannerRuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response data related to the creation of a rule.

        :param attributes: Attributes of the Sensitive Data Scanner rule.
        :type attributes: SensitiveDataScannerRuleAttributes, optional

        :param id: ID of the rule.
        :type id: str, optional

        :param relationships: Relationships of a scanning rule.
        :type relationships: SensitiveDataScannerRuleRelationships, optional

        :param type: Sensitive Data Scanner rule type.
        :type type: SensitiveDataScannerRuleType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
