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
    from datadog_api_client.v2.model.bill_config import BillConfig


class AzureUCConfigPostRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.bill_config import BillConfig

        return {
            "account_id": (str,),
            "actual_bill_config": (BillConfig,),
            "amortized_bill_config": (BillConfig,),
            "client_id": (str,),
            "scope": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "actual_bill_config": "actual_bill_config",
        "amortized_bill_config": "amortized_bill_config",
        "client_id": "client_id",
        "scope": "scope",
    }

    def __init__(
        self_,
        account_id: str,
        actual_bill_config: BillConfig,
        amortized_bill_config: BillConfig,
        client_id: str,
        scope: str,
        **kwargs,
    ):
        """
        Attributes for Azure config Post Request.

        :param account_id: The tenant ID of the Azure account.
        :type account_id: str

        :param actual_bill_config: Bill config.
        :type actual_bill_config: BillConfig

        :param amortized_bill_config: Bill config.
        :type amortized_bill_config: BillConfig

        :param client_id: The client ID of the Azure account.
        :type client_id: str

        :param scope: The scope of your observed subscription.
        :type scope: str
        """
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.actual_bill_config = actual_bill_config
        self_.amortized_bill_config = amortized_bill_config
        self_.client_id = client_id
        self_.scope = scope
