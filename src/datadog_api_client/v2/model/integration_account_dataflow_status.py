# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.integration_account_dataflow_health import IntegrationAccountDataflowHealth


class IntegrationAccountDataflowStatus(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.integration_account_dataflow_health import IntegrationAccountDataflowHealth

        return {
            "health": (IntegrationAccountDataflowHealth,),
            "message": (str,),
            "updated_at": (datetime,),
        }

    attribute_map = {
        "health": "health",
        "message": "message",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        health: Union[IntegrationAccountDataflowHealth, UnsetType] = unset,
        message: Union[str, UnsetType] = unset,
        updated_at: Union[datetime, UnsetType] = unset,
        **kwargs,
    ):
        """
        Read-only collection status of a dataflow.

        :param health: Collection health of a single dataflow.
        :type health: IntegrationAccountDataflowHealth, optional

        :param message: Human-readable detail, populated when the dataflow is not healthy.
        :type message: str, optional

        :param updated_at: Time the status was last computed.
        :type updated_at: datetime, optional
        """
        if health is not unset:
            kwargs["health"] = health
        if message is not unset:
            kwargs["message"] = message
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)
