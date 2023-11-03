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


class OutcomesBatchResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "total_received": (int,),
            "total_updated": (int,),
        }

    attribute_map = {
        "total_received": "total_received",
        "total_updated": "total_updated",
    }

    def __init__(
        self_, total_received: Union[int, UnsetType] = unset, total_updated: Union[int, UnsetType] = unset, **kwargs
    ):
        """
        Metadata pertaining to the bulk operation.

        :param total_received: Total number of scorecard results received during the bulk operation.
        :type total_received: int, optional

        :param total_updated: Total number of scorecard results modified during the bulk operation.
        :type total_updated: int, optional
        """
        if total_received is not unset:
            kwargs["total_received"] = total_received
        if total_updated is not unset:
            kwargs["total_updated"] = total_updated
        super().__init__(kwargs)
