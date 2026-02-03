# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


class WatchDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "application_id": (str,),
            "data_source": (str,),
            "event_id": (str,),
            "timestamp": (datetime,),
        }

    attribute_map = {
        "application_id": "application_id",
        "data_source": "data_source",
        "event_id": "event_id",
        "timestamp": "timestamp",
    }

    def __init__(
        self_,
        application_id: str,
        event_id: str,
        timestamp: datetime,
        data_source: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param application_id:
        :type application_id: str

        :param data_source:
        :type data_source: str, optional

        :param event_id:
        :type event_id: str

        :param timestamp:
        :type timestamp: datetime
        """
        if data_source is not unset:
            kwargs["data_source"] = data_source
        super().__init__(kwargs)

        self_.application_id = application_id
        self_.event_id = event_id
        self_.timestamp = timestamp
