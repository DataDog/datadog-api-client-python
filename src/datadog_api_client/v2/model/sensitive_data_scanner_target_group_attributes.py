# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sensitive_data_scanner_group_target import SensitiveDataScannerGroupTarget


class SensitiveDataScannerTargetGroupAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_group_target import SensitiveDataScannerGroupTarget

        return {
            "description": (str,),
            "is_enabled": (bool,),
            "name": (str,),
            "targets": ([SensitiveDataScannerGroupTarget],),
        }

    attribute_map = {
        "description": "description",
        "is_enabled": "is_enabled",
        "name": "name",
        "targets": "targets",
    }

    def __init__(
        self_, description: str, is_enabled: bool, name: str, targets: List[SensitiveDataScannerGroupTarget], **kwargs
    ):
        """
        Attributes of a scanning group of a target.

        :param description: Description of the group.
        :type description: str

        :param is_enabled: Whether or not the group is enabled.
        :type is_enabled: bool

        :param name: Name of the group.
        :type name: str

        :param targets: Targets the scanning group applies to. A scanning group has a single target for now.
        :type targets: [SensitiveDataScannerGroupTarget]
        """
        super().__init__(kwargs)

        self_.description = description
        self_.is_enabled = is_enabled
        self_.name = name
        self_.targets = targets
