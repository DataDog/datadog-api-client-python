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
    from datadog_api_client.v2.model.historical_job_response_data import HistoricalJobResponseData


class HistoricalJobResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.historical_job_response_data import HistoricalJobResponseData

        return {
            "data": (HistoricalJobResponseData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[HistoricalJobResponseData, UnsetType] = unset, **kwargs):
        """
        Historical job response.

        :param data: Historical job response data.
        :type data: HistoricalJobResponseData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
