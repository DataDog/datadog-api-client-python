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
    from datadog_api_client.v2.model.product_analytics_retention_list_record import ProductAnalyticsRetentionListRecord


class ProductAnalyticsRetentionListResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_retention_list_record import (
            ProductAnalyticsRetentionListRecord,
        )

        return {
            "records": ([ProductAnalyticsRetentionListRecord],),
            "retention_entity": (str,),
        }

    attribute_map = {
        "records": "records",
        "retention_entity": "retention_entity",
    }

    def __init__(
        self_,
        records: Union[List[ProductAnalyticsRetentionListRecord], UnsetType] = unset,
        retention_entity: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a retention list response, containing the matching entity rows.

        :param records: The matching entity rows.
        :type records: [ProductAnalyticsRetentionListRecord], optional

        :param retention_entity: The entity whose retention was measured.
        :type retention_entity: str, optional
        """
        if records is not unset:
            kwargs["records"] = records
        if retention_entity is not unset:
            kwargs["retention_entity"] = retention_entity
        super().__init__(kwargs)
