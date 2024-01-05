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
            "is_enabled": (bool,),
            "scope": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "actual_bill_config": "actual_bill_config",
        "amortized_bill_config": "amortized_bill_config",
        "client_id": "client_id",
        "is_enabled": "is_enabled",
        "scope": "scope",
    }

    def __init__(
        self_,
        account_id: str,
        actual_bill_config: BillConfig,
        amortized_bill_config: BillConfig,
        client_id: str,
        scope: str,
        is_enabled: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for Azure config Post Request.

        :param account_id: The tenant ID of the azure account.
        :type account_id: str

        :param actual_bill_config: Bill config.
        :type actual_bill_config: BillConfig

        :param amortized_bill_config: Bill config.
        :type amortized_bill_config: BillConfig

        :param client_id: The client ID of the azure account.
        :type client_id: str

        :param is_enabled: Whether or not the Cloud Cost Management account is enabled.
        :type is_enabled: bool, optional

        :param scope: The scope of your observed subscription.
        :type scope: str
        """
        if is_enabled is not unset:
            kwargs["is_enabled"] = is_enabled
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.actual_bill_config = actual_bill_config
        self_.amortized_bill_config = amortized_bill_config
        self_.client_id = client_id
        self_.scope = scope
