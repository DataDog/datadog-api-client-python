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
    from datadog_api_client.v1.model.aws_event_bridge_source import AWSEventBridgeSource


class AWSEventBridgeAccountConfiguration(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.aws_event_bridge_source import AWSEventBridgeSource

        return {
            "account_id": (str,),
            "event_hubs": ([AWSEventBridgeSource],),
            "tags": ([str],),
        }

    attribute_map = {
        "account_id": "accountId",
        "event_hubs": "eventHubs",
        "tags": "tags",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        event_hubs: Union[List[AWSEventBridgeSource], UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The EventBridge configuration for one AWS account.

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str, optional

        :param event_hubs: Array of AWS event sources associated with this account.
        :type event_hubs: [AWSEventBridgeSource], optional

        :param tags: Array of tags (in the form ``key:value`` ) which are added to all hosts
            and metrics reporting through the main AWS integration.
        :type tags: [str], optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if event_hubs is not unset:
            kwargs["event_hubs"] = event_hubs
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)
