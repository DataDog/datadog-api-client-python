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
    from datadog_api_client.v2.model.sensitive_data_scanner_target_group_data import SensitiveDataScannerTargetGroupData
    from datadog_api_client.v2.model.sensitive_data_scanner_rule_included_item import (
        SensitiveDataScannerRuleIncludedItem,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_meta import SensitiveDataScannerMeta


class SensitiveDataScannerTargetGroupResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_target_group_data import (
            SensitiveDataScannerTargetGroupData,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_rule_included_item import (
            SensitiveDataScannerRuleIncludedItem,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_meta import SensitiveDataScannerMeta

        return {
            "data": (SensitiveDataScannerTargetGroupData,),
            "included": ([SensitiveDataScannerRuleIncludedItem],),
            "meta": (SensitiveDataScannerMeta,),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: SensitiveDataScannerTargetGroupData,
        meta: SensitiveDataScannerMeta,
        included: Union[List[SensitiveDataScannerRuleIncludedItem], UnsetType] = unset,
        **kwargs,
    ):
        """
        A scanning group of a target, with its rules included.

        :param data: A scanning group of a target.
        :type data: SensitiveDataScannerTargetGroupData

        :param included: Rules of the returned groups.
        :type included: [SensitiveDataScannerRuleIncludedItem], optional

        :param meta: Meta response. Always an empty object.
        :type meta: SensitiveDataScannerMeta
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
        self_.meta = meta
