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
    from datadog_api_client.v1.model.aws_event_bridge_account_configuration import AWSEventBridgeAccountConfiguration


class AWSEventBridgeListResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_event_bridge_account_configuration import (
            AWSEventBridgeAccountConfiguration,
        )

        return {
            "accounts": ([AWSEventBridgeAccountConfiguration],),
            "is_installed": (bool,),
        }

    attribute_map = {
        "accounts": "accounts",
        "is_installed": "isInstalled",
    }

    def __init__(
        self_,
        accounts: Union[List[AWSEventBridgeAccountConfiguration], UnsetType] = unset,
        is_installed: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        An object describing the EventBridge configuration for multiple accounts.

        :param accounts: List of accounts with their event sources.
        :type accounts: [AWSEventBridgeAccountConfiguration], optional

        :param is_installed: True if the EventBridge sub-integration is enabled for your organization.
        :type is_installed: bool, optional
        """
        if accounts is not unset:
            kwargs["accounts"] = accounts
        if is_installed is not unset:
            kwargs["is_installed"] = is_installed
        super().__init__(kwargs)
