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
    from datadog_api_client.v2.model.quota_limit import QuotaLimit
    from datadog_api_client.v2.model.quota_processor_override import QuotaProcessorOverride
    from datadog_api_client.v2.model.quota_processor_type import QuotaProcessorType


class QuotaProcessor(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.quota_limit import QuotaLimit
        from datadog_api_client.v2.model.quota_processor_override import QuotaProcessorOverride
        from datadog_api_client.v2.model.quota_processor_type import QuotaProcessorType

        return {
            "drop_events": (bool,),
            "id": (str,),
            "ignore_when_missing_partitions": (bool,),
            "inputs": ([str],),
            "limit": (QuotaLimit,),
            "name": (str,),
            "overrides": ([QuotaProcessorOverride],),
            "partition_fields": ([str],),
            "type": (QuotaProcessorType,),
        }

    attribute_map = {
        "drop_events": "drop_events",
        "id": "id",
        "ignore_when_missing_partitions": "ignore_when_missing_partitions",
        "inputs": "inputs",
        "limit": "limit",
        "name": "name",
        "overrides": "overrides",
        "partition_fields": "partition_fields",
        "type": "type",
    }

    def __init__(
        self_,
        drop_events: bool,
        id: str,
        inputs: List[str],
        limit: QuotaLimit,
        name: str,
        type: QuotaProcessorType,
        ignore_when_missing_partitions: Union[bool, UnsetType] = unset,
        overrides: Union[List[QuotaProcessorOverride], UnsetType] = unset,
        partition_fields: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        The Quota Processor measures logging traffic for logs that match a specified filter. When the configured daily quota is met, the processor can drop or alert.

        :param drop_events: The ``QuotaProcessor`` ``drop_events``.
        :type drop_events: bool

        :param id: Unique identifier.
        :type id: str

        :param ignore_when_missing_partitions: The ``QuotaProcessor`` ``ignore_when_missing_partitions``.
        :type ignore_when_missing_partitions: bool, optional

        :param inputs: The ``QuotaProcessor`` ``inputs``.
        :type inputs: [str]

        :param limit: Unified definition of ``QuotaLimit`` object.
        :type limit: QuotaLimit

        :param name: The ``QuotaProcessor`` ``name``.
        :type name: str

        :param overrides: The ``QuotaProcessor`` ``overrides``.
        :type overrides: [QuotaProcessorOverride], optional

        :param partition_fields: The ``QuotaProcessor`` ``partition_fields``.
        :type partition_fields: [str], optional

        :param type: The definition of ``QuotaProcessorType`` object.
        :type type: QuotaProcessorType
        """
        if ignore_when_missing_partitions is not unset:
            kwargs["ignore_when_missing_partitions"] = ignore_when_missing_partitions
        if overrides is not unset:
            kwargs["overrides"] = overrides
        if partition_fields is not unset:
            kwargs["partition_fields"] = partition_fields
        super().__init__(kwargs)

        self_.drop_events = drop_events
        self_.id = id
        self_.inputs = inputs
        self_.limit = limit
        self_.name = name
        self_.type = type
