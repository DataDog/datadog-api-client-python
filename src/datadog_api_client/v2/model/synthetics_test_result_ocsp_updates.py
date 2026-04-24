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


class SyntheticsTestResultOCSPUpdates(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_update": (int,),
            "produced_at": (int,),
            "this_update": (int,),
        }

    attribute_map = {
        "next_update": "next_update",
        "produced_at": "produced_at",
        "this_update": "this_update",
    }

    def __init__(
        self_,
        next_update: Union[int, UnsetType] = unset,
        produced_at: Union[int, UnsetType] = unset,
        this_update: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        OCSP response update timestamps.

        :param next_update: Unix timestamp (ms) of the next expected OCSP update.
        :type next_update: int, optional

        :param produced_at: Unix timestamp (ms) of when the OCSP response was produced.
        :type produced_at: int, optional

        :param this_update: Unix timestamp (ms) of this OCSP update.
        :type this_update: int, optional
        """
        if next_update is not unset:
            kwargs["next_update"] = next_update
        if produced_at is not unset:
            kwargs["produced_at"] = produced_at
        if this_update is not unset:
            kwargs["this_update"] = this_update
        super().__init__(kwargs)
