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
    from datadog_api_client.v1.model.synthetics_uptime import SyntheticsUptime


class SyntheticsTestUptime(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.synthetics_uptime import SyntheticsUptime

        return {
            "from_ts": (int,),
            "overall": (SyntheticsUptime,),
            "public_id": (str,),
            "to_ts": (int,),
        }

    attribute_map = {
        "from_ts": "from_ts",
        "overall": "overall",
        "public_id": "public_id",
        "to_ts": "to_ts",
    }

    def __init__(
        self_,
        from_ts: Union[int, UnsetType] = unset,
        overall: Union[SyntheticsUptime, UnsetType] = unset,
        public_id: Union[str, UnsetType] = unset,
        to_ts: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Object containing the uptime for a Synthetic test ID.

        :param from_ts: Timestamp in seconds for the start of uptime.
        :type from_ts: int, optional

        :param overall: Object containing the uptime information.
        :type overall: SyntheticsUptime, optional

        :param public_id: A Synthetic test ID.
        :type public_id: str, optional

        :param to_ts: Timestamp in seconds for the end of uptime.
        :type to_ts: int, optional
        """
        if from_ts is not unset:
            kwargs["from_ts"] = from_ts
        if overall is not unset:
            kwargs["overall"] = overall
        if public_id is not unset:
            kwargs["public_id"] = public_id
        if to_ts is not unset:
            kwargs["to_ts"] = to_ts
        super().__init__(kwargs)
