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
    from datadog_api_client.v2.model.sensitive_data_scanner_filter import SensitiveDataScannerFilter
    from datadog_api_client.v2.model.sensitive_data_scanner_group_target import SensitiveDataScannerGroupTarget
    from datadog_api_client.v2.model.sensitive_data_scanner_samplings import SensitiveDataScannerSamplings


class SensitiveDataScannerTargetGroupAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_filter import SensitiveDataScannerFilter
        from datadog_api_client.v2.model.sensitive_data_scanner_group_target import SensitiveDataScannerGroupTarget
        from datadog_api_client.v2.model.sensitive_data_scanner_samplings import SensitiveDataScannerSamplings

        return {
            "description": (str,),
            "filter": (SensitiveDataScannerFilter,),
            "is_enabled": (bool,),
            "name": (str,),
            "product_list": ([SensitiveDataScannerGroupTarget],),
            "samplings": ([SensitiveDataScannerSamplings],),
        }

    attribute_map = {
        "description": "description",
        "filter": "filter",
        "is_enabled": "is_enabled",
        "name": "name",
        "product_list": "product_list",
        "samplings": "samplings",
    }

    def __init__(
        self_,
        description: str,
        filter: SensitiveDataScannerFilter,
        is_enabled: bool,
        name: str,
        product_list: List[SensitiveDataScannerGroupTarget],
        samplings: List[SensitiveDataScannerSamplings],
        **kwargs,
    ):
        """
        Attributes of a scanning group of a target.

        :param description: Description of the group.
        :type description: str

        :param filter: Filter for the Scanning Group.
        :type filter: SensitiveDataScannerFilter

        :param is_enabled: Whether or not the group is enabled.
        :type is_enabled: bool

        :param name: Name of the group.
        :type name: str

        :param product_list: Products the scanning group applies to.
        :type product_list: [SensitiveDataScannerGroupTarget]

        :param samplings: Sampling rates per product type. Always empty for these targets.
        :type samplings: [SensitiveDataScannerSamplings]
        """
        super().__init__(kwargs)

        self_.description = description
        self_.filter = filter
        self_.is_enabled = is_enabled
        self_.name = name
        self_.product_list = product_list
        self_.samplings = samplings
