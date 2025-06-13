# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class JobDefinitionFromRule(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (int,),
            "id": (str,),
            "index": (str,),
            "notifications": ([str],),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "id": "id",
        "index": "index",
        "notifications": "notifications",
        "to": "to",
    }

    def __init__(
        self_, _from: int, id: str, index: str, to: int, notifications: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        Definition of a historical job based on a security monitoring rule.

        :param _from: Starting time of data analyzed by the job.
        :type _from: int

        :param id: ID of the detection rule used to create the job.
        :type id: str

        :param index: Index used to load the data.
        :type index: str

        :param notifications: Notifications sent when the job is completed.
        :type notifications: [str], optional

        :param to: Ending time of data analyzed by the job.
        :type to: int
        """
        if notifications is not unset:
            kwargs["notifications"] = notifications
        super().__init__(kwargs)

        self_._from = _from
        self_.id = id
        self_.index = index
        self_.to = to
