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
    from datadog_api_client.v2.model.cpu import Cpu


class Estimation(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cpu import Cpu

        return {
            "cpu": (Cpu,),
            "ephemeral_storage": (int,),
            "heap": (int,),
            "memory": (int,),
            "overhead": (int,),
        }

    attribute_map = {
        "cpu": "cpu",
        "ephemeral_storage": "ephemeral_storage",
        "heap": "heap",
        "memory": "memory",
        "overhead": "overhead",
    }

    def __init__(
        self_,
        cpu: Union[Cpu, UnsetType] = unset,
        ephemeral_storage: Union[int, UnsetType] = unset,
        heap: Union[int, UnsetType] = unset,
        memory: Union[int, UnsetType] = unset,
        overhead: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Recommended resource values for a Spark driver or executor, derived from recent real usage metrics. Used by SPA to propose more efficient pod sizing.

        :param cpu: CPU usage statistics derived from historical Spark job metrics. Provides multiple estimates so users can choose between conservative and cost-saving risk profiles.
        :type cpu: Cpu, optional

        :param ephemeral_storage: Recommended ephemeral storage allocation (in MiB). Derived from job temporary storage patterns.
        :type ephemeral_storage: int, optional

        :param heap: Recommended JVM heap size (in MiB).
        :type heap: int, optional

        :param memory: Recommended total memory allocation (in MiB). Includes both heap and overhead.
        :type memory: int, optional

        :param overhead: Recommended JVM overhead (in MiB). Computed as total memory - heap.
        :type overhead: int, optional
        """
        if cpu is not unset:
            kwargs["cpu"] = cpu
        if ephemeral_storage is not unset:
            kwargs["ephemeral_storage"] = ephemeral_storage
        if heap is not unset:
            kwargs["heap"] = heap
        if memory is not unset:
            kwargs["memory"] = memory
        if overhead is not unset:
            kwargs["overhead"] = overhead
        super().__init__(kwargs)
