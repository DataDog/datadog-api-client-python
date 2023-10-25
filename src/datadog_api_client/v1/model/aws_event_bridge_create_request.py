# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class AWSEventBridgeCreateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "account_id": (str,),
            "create_event_bus": (bool,),
            "event_generator_name": (str,),
            "region": (str,),
        }

    attribute_map = {
        "account_id": "account_id",
        "create_event_bus": "create_event_bus",
        "event_generator_name": "event_generator_name",
        "region": "region",
    }

    def __init__(
        self_,
        account_id: Union[str, UnsetType] = unset,
        create_event_bus: Union[bool, UnsetType] = unset,
        event_generator_name: Union[str, UnsetType] = unset,
        region: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        An object used to create an EventBridge source.

        :param account_id: Your AWS Account ID without dashes.
        :type account_id: str, optional

        :param create_event_bus: True if Datadog should create the event bus in addition to the event
            source. Requires the ``events:CreateEventBus`` permission.
        :type create_event_bus: bool, optional

        :param event_generator_name: The given part of the event source name, which is then combined with an
            assigned suffix to form the full name.
        :type event_generator_name: str, optional

        :param region: The event source's `AWS region <https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints>`_.
        :type region: str, optional
        """
        if account_id is not unset:
            kwargs["account_id"] = account_id
        if create_event_bus is not unset:
            kwargs["create_event_bus"] = create_event_bus
        if event_generator_name is not unset:
            kwargs["event_generator_name"] = event_generator_name
        if region is not unset:
            kwargs["region"] = region
        super().__init__(kwargs)
