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
    from datadog_api_client.v2.model.historical_job_response_data import HistoricalJobResponseData
    from datadog_api_client.v2.model.historical_job_list_meta import HistoricalJobListMeta


class ListHistoricalJobsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.historical_job_response_data import HistoricalJobResponseData
        from datadog_api_client.v2.model.historical_job_list_meta import HistoricalJobListMeta

        return {
            "data": ([HistoricalJobResponseData],),
            "meta": (HistoricalJobListMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(
        self_,
        data: Union[List[HistoricalJobResponseData], UnsetType] = unset,
        meta: Union[HistoricalJobListMeta, UnsetType] = unset,
        **kwargs,
    ):
        """
        List of historical jobs.

        :param data: Array containing the list of historical jobs.
        :type data: [HistoricalJobResponseData], optional

        :param meta: Metadata about the list of jobs.
        :type meta: HistoricalJobListMeta, optional
        """
        if data is not unset:
            kwargs["data"] = data
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)
