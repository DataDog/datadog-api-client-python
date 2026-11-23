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
    from datadog_api_client.v2.model.sensitive_data_scanner_group_data import SensitiveDataScannerGroupData
    from datadog_api_client.v2.model.sensitive_data_scanner_standard_rule import SensitiveDataScannerStandardRule


class SensitiveDataScannerTargetRuleRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_group_data import SensitiveDataScannerGroupData
        from datadog_api_client.v2.model.sensitive_data_scanner_standard_rule import SensitiveDataScannerStandardRule

        return {
            "group": (SensitiveDataScannerGroupData,),
            "standard_rule": (SensitiveDataScannerStandardRule,),
        }

    attribute_map = {
        "group": "group",
        "standard_rule": "standard_rule",
    }

    def __init__(
        self_,
        group: Union[SensitiveDataScannerGroupData, UnsetType] = unset,
        standard_rule: Union[SensitiveDataScannerStandardRule, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of a rule of a scanning group of a target.

        :param group: A scanning group data.
        :type group: SensitiveDataScannerGroupData, optional

        :param standard_rule: The standard rule a rule is based on. Not included for custom rules.
        :type standard_rule: SensitiveDataScannerStandardRule, optional
        """
        if group is not unset:
            kwargs["group"] = group
        if standard_rule is not unset:
            kwargs["standard_rule"] = standard_rule
        super().__init__(kwargs)
