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
    from datadog_api_client.v2.model.run_historical_job_request_attributes import RunHistoricalJobRequestAttributes
    from datadog_api_client.v2.model.run_historical_job_request_data_type import RunHistoricalJobRequestDataType


class RunHistoricalJobRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.run_historical_job_request_attributes import RunHistoricalJobRequestAttributes
        from datadog_api_client.v2.model.run_historical_job_request_data_type import RunHistoricalJobRequestDataType

        return {
            "attributes": (RunHistoricalJobRequestAttributes,),
            "type": (RunHistoricalJobRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[RunHistoricalJobRequestAttributes, UnsetType] = unset,
        type: Union[RunHistoricalJobRequestDataType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Data for running a historical job request.

        :param attributes: Run a historical job request.
        :type attributes: RunHistoricalJobRequestAttributes, optional

        :param type: Type of data.
        :type type: RunHistoricalJobRequestDataType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
