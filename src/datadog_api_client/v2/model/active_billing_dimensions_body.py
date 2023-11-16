# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.active_billing_dimensions_attributes import ActiveBillingDimensionsAttributes
    from datadog_api_client.v2.model.active_billing_dimensions_type import ActiveBillingDimensionsType


class ActiveBillingDimensionsBody(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.active_billing_dimensions_attributes import ActiveBillingDimensionsAttributes
        from datadog_api_client.v2.model.active_billing_dimensions_type import ActiveBillingDimensionsType

        return {
            "attributes": (ActiveBillingDimensionsAttributes,),
            "id": (str,),
            "type": (ActiveBillingDimensionsType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[ActiveBillingDimensionsAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ActiveBillingDimensionsType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Active billing dimensions data.

        :param attributes: List of active billing dimensions.
        :type attributes: ActiveBillingDimensionsAttributes, optional

        :param id: Unique ID of the response.
        :type id: str, optional

        :param type: Type of active billing dimensions data.
        :type type: ActiveBillingDimensionsType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
