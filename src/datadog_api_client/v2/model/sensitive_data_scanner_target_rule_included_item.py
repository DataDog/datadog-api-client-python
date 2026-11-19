# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sensitive_data_scanner_target_rule_attributes import (
        SensitiveDataScannerTargetRuleAttributes,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_target_rule_relationships import (
        SensitiveDataScannerTargetRuleRelationships,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType
    from datadog_api_client.v2.model.sensitive_data_scanner_custom_regex_rule_attributes import (
        SensitiveDataScannerCustomRegexRuleAttributes,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_standard_regex_rule_attributes import (
        SensitiveDataScannerStandardRegexRuleAttributes,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_machine_learning_rule_attributes import (
        SensitiveDataScannerMachineLearningRuleAttributes,
    )


class SensitiveDataScannerTargetRuleIncludedItem(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_target_rule_attributes import (
            SensitiveDataScannerTargetRuleAttributes,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_target_rule_relationships import (
            SensitiveDataScannerTargetRuleRelationships,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_rule_type import SensitiveDataScannerRuleType

        return {
            "attributes": (SensitiveDataScannerTargetRuleAttributes,),
            "id": (str,),
            "relationships": (SensitiveDataScannerTargetRuleRelationships,),
            "type": (SensitiveDataScannerRuleType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[
            SensitiveDataScannerTargetRuleAttributes,
            SensitiveDataScannerCustomRegexRuleAttributes,
            SensitiveDataScannerStandardRegexRuleAttributes,
            SensitiveDataScannerMachineLearningRuleAttributes,
            UnsetType,
        ] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[SensitiveDataScannerTargetRuleRelationships, UnsetType] = unset,
        type: Union[SensitiveDataScannerRuleType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A rule of a scanning group of a target.

        :param attributes: Attributes of a rule of a scanning group of a target. They depend on the type of rule.
        :type attributes: SensitiveDataScannerTargetRuleAttributes, optional

        :param id: ID of the rule.
        :type id: str, optional

        :param relationships: Relationships of a rule of a scanning group of a target.
        :type relationships: SensitiveDataScannerTargetRuleRelationships, optional

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
