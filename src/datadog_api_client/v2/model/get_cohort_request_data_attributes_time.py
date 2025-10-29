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


class GetCohortRequestDataAttributesTime(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "_from": (int,),
            "to": (int,),
        }

    attribute_map = {
        "_from": "from",
        "to": "to",
    }

    def __init__(self_, _from: Union[int, UnsetType] = unset, to: Union[int, UnsetType] = unset, **kwargs):
        """


        :param _from:
        :type _from: int, optional

        :param to:
        :type to: int, optional
        """
        if _from is not unset:
            kwargs["_from"] = _from
        if to is not unset:
            kwargs["to"] = to
        super().__init__(kwargs)
