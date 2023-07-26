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
    from datadog_api_client.v2.model.on_demand_concurrency_cap_attributes import OnDemandConcurrencyCapAttributes
    from datadog_api_client.v2.model.on_demand_concurrency_cap_type import OnDemandConcurrencyCapType


class OnDemandConcurrencyCap(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.on_demand_concurrency_cap_attributes import OnDemandConcurrencyCapAttributes
        from datadog_api_client.v2.model.on_demand_concurrency_cap_type import OnDemandConcurrencyCapType

        return {
            "attributes": (OnDemandConcurrencyCapAttributes,),
            "type": (OnDemandConcurrencyCapType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[OnDemandConcurrencyCapAttributes, UnsetType] = unset,
        type: Union[OnDemandConcurrencyCapType, UnsetType] = unset,
        **kwargs,
    ):
        """
        On-demand concurrency cap.

        :param attributes: On-demand concurrency cap attributes.
        :type attributes: OnDemandConcurrencyCapAttributes, optional

        :param type: On-demand concurrency cap type.
        :type type: OnDemandConcurrencyCapType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
