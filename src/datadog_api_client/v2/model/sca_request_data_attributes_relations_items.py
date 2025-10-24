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


class ScaRequestDataAttributesRelationsItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "depends_on": ([str],),
            "ref": (str,),
        }

    attribute_map = {
        "depends_on": "depends_on",
        "ref": "ref",
    }

    def __init__(self_, depends_on: Union[List[str], UnsetType] = unset, ref: Union[str, UnsetType] = unset, **kwargs):
        """


        :param depends_on:
        :type depends_on: [str], optional

        :param ref:
        :type ref: str, optional
        """
        if depends_on is not unset:
            kwargs["depends_on"] = depends_on
        if ref is not unset:
            kwargs["ref"] = ref
        super().__init__(kwargs)
