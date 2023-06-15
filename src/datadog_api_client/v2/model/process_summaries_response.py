# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.process_summary import ProcessSummary
    from datadog_api_client.v2.model.process_summaries_meta import ProcessSummariesMeta


@dataclass
class ProcessSummariesResponseJSON:
    id: str
    cmdline: Union[str, UnsetType] = unset
    host: Union[str, UnsetType] = unset
    pid: Union[int, UnsetType] = unset
    ppid: Union[int, UnsetType] = unset
    start: Union[str, UnsetType] = unset
    tags: Union[List[str], UnsetType] = unset
    timestamp: Union[str, UnsetType] = unset
    user: Union[str, UnsetType] = unset


class ProcessSummariesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.process_summary import ProcessSummary
        from datadog_api_client.v2.model.process_summaries_meta import ProcessSummariesMeta

        return {
            "data": ([ProcessSummary],),
            "meta": (ProcessSummariesMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }
    json_api_model = ProcessSummariesResponseJSON

    def __init__(
        self_,
        data: Union[List[ProcessSummary], UnsetType] = unset,
        meta: Union[ProcessSummariesMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of process summaries.

        :param data: Array of process summary objects.
        :type data: [ProcessSummary], optional

        :param meta: Response metadata object.
        :type meta: ProcessSummariesMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
