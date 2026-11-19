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
    from datadog_api_client.v2.model.sensitive_data_scanner_standard_rule_data import (
        SensitiveDataScannerStandardRuleData,
    )


class SensitiveDataScannerStandardRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_standard_rule_data import (
            SensitiveDataScannerStandardRuleData,
        )

        return {
            "data": (SensitiveDataScannerStandardRuleData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[SensitiveDataScannerStandardRuleData, UnsetType] = unset, **kwargs):
        """
        The standard rule a rule is based on. Not included for custom rules.

        :param data: A standard rule.
        :type data: SensitiveDataScannerStandardRuleData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
