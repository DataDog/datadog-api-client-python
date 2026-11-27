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
    from datadog_api_client.v2.model.sensitive_data_scanner_group_target_type import SensitiveDataScannerGroupTargetType


class SensitiveDataScannerGroupTarget(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_group_target_type import (
            SensitiveDataScannerGroupTargetType,
        )

        return {
            "type": (SensitiveDataScannerGroupTargetType,),
        }

    attribute_map = {
        "type": "type",
    }

    def __init__(self_, type: SensitiveDataScannerGroupTargetType, **kwargs):
        """
        A target the scanning group applies to.

        :param type: Type of target whose scanning groups are served by the target-scoped group routes. ``llm_observability`` is Agent Observability, ``ai_guard`` is AI Guard.
        :type type: SensitiveDataScannerGroupTargetType
        """
        super().__init__(kwargs)

        self_.type = type
