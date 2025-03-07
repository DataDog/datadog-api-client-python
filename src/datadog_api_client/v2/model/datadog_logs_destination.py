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
    from datadog_api_client.v2.model.datadog_logs_destination_type import DatadogLogsDestinationType


class DatadogLogsDestination(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.datadog_logs_destination_type import DatadogLogsDestinationType

        return {
            "id": (str,),
            "inputs": ([str],),
            "type": (DatadogLogsDestinationType,),
        }

    attribute_map = {
        "id": "id",
        "inputs": "inputs",
        "type": "type",
    }

    def __init__(
        self_, id: str, type: DatadogLogsDestinationType, inputs: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        A Datadog Logs destination component.

        :param id: The unique ID of the destination.
        :type id: str

        :param inputs: The inputs for the destination.
        :type inputs: [str], optional

        :param type: The type of destination.
        :type type: DatadogLogsDestinationType
        """
        if inputs is not unset:
            kwargs["inputs"] = inputs
        super().__init__(kwargs)

        self_.id = id
        self_.type = type
