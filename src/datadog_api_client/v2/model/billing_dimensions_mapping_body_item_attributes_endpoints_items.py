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
    from datadog_api_client.v2.model.billing_dimensions_mapping_body_item_attributes_endpoints_items_status import (
        BillingDimensionsMappingBodyItemAttributesEndpointsItemsStatus,
    )


class BillingDimensionsMappingBodyItemAttributesEndpointsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.billing_dimensions_mapping_body_item_attributes_endpoints_items_status import (
            BillingDimensionsMappingBodyItemAttributesEndpointsItemsStatus,
        )

        return {
            "id": (str,),
            "keys": ([str],),
            "status": (BillingDimensionsMappingBodyItemAttributesEndpointsItemsStatus,),
        }

    attribute_map = {
        "id": "id",
        "keys": "keys",
        "status": "status",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        keys: Union[List[str], UnsetType] = unset,
        status: Union[BillingDimensionsMappingBodyItemAttributesEndpointsItemsStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        An endpoint's keys mapped to the billing_dimension.

        :param id: The URL for the endpoint.
        :type id: str, optional

        :param keys: The billing dimension.
        :type keys: [str], optional

        :param status: Denotes whether mapping keys were available for this endpoint.
        :type status: BillingDimensionsMappingBodyItemAttributesEndpointsItemsStatus, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if keys is not unset:
            kwargs["keys"] = keys
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
