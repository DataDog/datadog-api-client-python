# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class SyntheticsTestResultLocation(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "id": (str,),
            "name": (str,),
            "version": (str,),
            "worker_id": (str,),
        }

    attribute_map = {
        "id": "id",
        "name": "name",
        "version": "version",
        "worker_id": "worker_id",
    }

    def __init__(
        self_,
        id: Union[str, UnsetType] = unset,
        name: Union[str, UnsetType] = unset,
        version: Union[str, UnsetType] = unset,
        worker_id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Location information for a Synthetic test result.

        :param id: Identifier of the location.
        :type id: str, optional

        :param name: Human-readable name of the location.
        :type name: str, optional

        :param version: Version of the worker that ran the test.
        :type version: str, optional

        :param worker_id: Identifier of the specific worker that ran the test.
        :type worker_id: str, optional
        """
        if id is not unset:
            kwargs["id"] = id
        if name is not unset:
            kwargs["name"] = name
        if version is not unset:
            kwargs["version"] = version
        if worker_id is not unset:
            kwargs["worker_id"] = worker_id
        super().__init__(kwargs)
