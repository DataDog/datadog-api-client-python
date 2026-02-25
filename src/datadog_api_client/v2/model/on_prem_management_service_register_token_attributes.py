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
    UUID,
)


class OnPremManagementServiceRegisterTokenAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "app_id": (UUID,),
            "app_version": (int,),
            "connection_id": (UUID,),
            "query_id": (UUID,),
            "runner_id": (str,),
        }

    attribute_map = {
        "app_id": "app_id",
        "app_version": "app_version",
        "connection_id": "connection_id",
        "query_id": "query_id",
        "runner_id": "runner_id",
    }

    def __init__(
        self_,
        connection_id: UUID,
        runner_id: str,
        app_id: Union[UUID, UnsetType] = unset,
        app_version: Union[int, UnsetType] = unset,
        query_id: Union[UUID, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for registering a token.

        :param app_id: The application identifier.
        :type app_id: UUID, optional

        :param app_version: The application version.
        :type app_version: int, optional

        :param connection_id: The connection identifier.
        :type connection_id: UUID

        :param query_id: The query identifier.
        :type query_id: UUID, optional

        :param runner_id: The on-prem runner identifier.
        :type runner_id: str
        """
        if app_id is not unset:
            kwargs["app_id"] = app_id
        if app_version is not unset:
            kwargs["app_version"] = app_version
        if query_id is not unset:
            kwargs["query_id"] = query_id
        super().__init__(kwargs)

        self_.connection_id = connection_id
        self_.runner_id = runner_id
