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
    from datadog_api_client.v2.model.cost_currency_type import CostCurrencyType


class CostCurrency(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_currency_type import CostCurrencyType

        return {
            "id": (str,),
            "type": (CostCurrencyType,),
        }

    attribute_map = {
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id: str, type: CostCurrencyType, **kwargs):
        """
        A Cloud Cost Management billing currency entry.

        :param id: The currency code (for example, ``USD`` ).
        :type id: str

        :param type: Type of the Cloud Cost Management billing currency resource.
        :type type: CostCurrencyType
        """
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
