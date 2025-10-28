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


class AWSEventBridgeCreateRequestAttributes(ModelNormal):
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
        account_id: str,
        event_generator_name: str,
        region: str,
        create_event_bus: Union[bool, UnsetType] = unset,
        **kwargs,
    ):
        """
        The EventBridge source to be created.

        :param account_id: AWS Account ID.
        :type account_id: str

        :param create_event_bus: Set to true if Datadog should create the event bus in addition to the event
            source. Requires the ``events:CreateEventBus`` permission.
        :type create_event_bus: bool, optional

        :param event_generator_name: The given part of the event source name, which is then combined with an
            assigned suffix to form the full name.
        :type event_generator_name: str

        :param region: The event source's
            `AWS region <https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints>`_.
        :type region: str
        """
        if create_event_bus is not unset:
            kwargs["create_event_bus"] = create_event_bus
        super().__init__(kwargs)

        self_.account_id = account_id
        self_.event_generator_name = event_generator_name
        self_.region = region
