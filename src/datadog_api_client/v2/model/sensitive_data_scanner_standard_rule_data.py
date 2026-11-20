# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sensitive_data_scanner_standard_rule_type import (
        SensitiveDataScannerStandardRuleType,
    )


class SensitiveDataScannerStandardRuleData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_standard_rule_type import (
            SensitiveDataScannerStandardRuleType,
        )

        return {
            "id": (str,),
            "type": (SensitiveDataScannerStandardRuleType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: SensitiveDataScannerStandardRuleType, **kwargs):
        """
        A standard rule.

        :param id: ID of the standard rule.
        :type id: str

        :param type: Type of standard rule, based on how it detects sensitive data.
        :type type: SensitiveDataScannerStandardRuleType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
