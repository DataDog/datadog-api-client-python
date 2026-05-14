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


class IncidentCommunicationContentHandle(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (str,),
            "display_name": (str,),
            "handle": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "display_name": "display_name",
        "handle": "handle",
    }

    def __init__(
        self_,
        handle: str,
        created_at: Union[str, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A handle used for sending a communication.

        :param created_at: Timestamp when the handle was added.
        :type created_at: str, optional

        :param display_name: The display name for the handle.
        :type display_name: str, optional

        :param handle: The notification handle.
        :type handle: str
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if display_name is not unset:
            kwargs["display_name"] = display_name
        super().__init__(kwargs)

        self_.handle = handle
