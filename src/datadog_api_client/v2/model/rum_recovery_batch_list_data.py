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
    from datadog_api_client.v2.model.rum_recovery_batch_list_attributes import RUMRecoveryBatchListAttributes
    from datadog_api_client.v2.model.rum_recovery_batch_list_data_type import RUMRecoveryBatchListDataType


class RUMRecoveryBatchListData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_recovery_batch_list_attributes import RUMRecoveryBatchListAttributes
        from datadog_api_client.v2.model.rum_recovery_batch_list_data_type import RUMRecoveryBatchListDataType

        return {
            "attributes": (RUMRecoveryBatchListAttributes,),
            "id": (str,),
            "type": (RUMRecoveryBatchListDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_, attributes: RUMRecoveryBatchListAttributes, id: str, type: RUMRecoveryBatchListDataType, **kwargs
    ):
        """
        JSON:API resource.

        :param attributes: Batch recovery progress. Status updates can appear here before they appear in request details.
        :type attributes: RUMRecoveryBatchListAttributes

        :param id: Resource identifier.
        :type id: str

        :param type: JSON:API resource type.
        :type type: RUMRecoveryBatchListDataType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.id = id
        self_.type = type
