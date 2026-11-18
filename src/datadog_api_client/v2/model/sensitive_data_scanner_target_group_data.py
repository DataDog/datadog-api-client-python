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
    from datadog_api_client.v2.model.sensitive_data_scanner_target_group_attributes import (
        SensitiveDataScannerTargetGroupAttributes,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_target_group_relationships import (
        SensitiveDataScannerTargetGroupRelationships,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType


class SensitiveDataScannerTargetGroupData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_target_group_attributes import (
            SensitiveDataScannerTargetGroupAttributes,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_target_group_relationships import (
            SensitiveDataScannerTargetGroupRelationships,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_group_type import SensitiveDataScannerGroupType

        return {
            "attributes": (SensitiveDataScannerTargetGroupAttributes,),
            "id": (str,),
            "relationships": (SensitiveDataScannerTargetGroupRelationships,),
            "type": (SensitiveDataScannerGroupType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: SensitiveDataScannerTargetGroupAttributes,
        id: str,
        relationships: SensitiveDataScannerTargetGroupRelationships,
        type: SensitiveDataScannerGroupType,
        **kwargs,
    ):
        """
        A scanning group of a target.

        :param attributes: Attributes of a scanning group of a target.
        :type attributes: SensitiveDataScannerTargetGroupAttributes

        :param id: ID of the group.
        :type id: str

        :param relationships: Relationships of a scanning group of a target.
        :type relationships: SensitiveDataScannerTargetGroupRelationships

        :param type: Sensitive Data Scanner group type.
        :type type: SensitiveDataScannerGroupType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.relationships = relationships
        self_.type = type
