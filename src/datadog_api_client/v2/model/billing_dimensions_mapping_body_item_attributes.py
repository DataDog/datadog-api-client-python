# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.billing_dimensions_mapping_body_item_attributes_endpoints_items import (
        BillingDimensionsMappingBodyItemAttributesEndpointsItems,
    )


class BillingDimensionsMappingBodyItemAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.billing_dimensions_mapping_body_item_attributes_endpoints_items import (
            BillingDimensionsMappingBodyItemAttributesEndpointsItems,
        )

        return {
            "endpoints": ([BillingDimensionsMappingBodyItemAttributesEndpointsItems],),
            "in_app_label": (str,),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "endpoints": "endpoints",
        "in_app_label": "in_app_label",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        endpoints: Union[List[BillingDimensionsMappingBodyItemAttributesEndpointsItems], UnsetType] = unset,
        in_app_label: Union[str, UnsetType] = unset,
        timestamp: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Mapping of billing dimensions to endpoint keys.

        :param endpoints: List of supported endpoints with their keys mapped to the billing_dimension.
        :type endpoints: [BillingDimensionsMappingBodyItemAttributesEndpointsItems], optional

        :param in_app_label: Label used for the billing dimension in the Plan & Usage charts.
        :type in_app_label: str, optional

        :param timestamp: Month in ISO-8601 format, UTC, and precise to the second: ``[YYYY-MM-DDThh:mm:ss]``.
        :type timestamp: datetime, optional
        """
        if endpoints is not unset:
            kwargs["endpoints"] = endpoints
        if in_app_label is not unset:
            kwargs["in_app_label"] = in_app_label
        if timestamp is not unset:
            kwargs["timestamp"] = timestamp
        super().__init__(kwargs)
