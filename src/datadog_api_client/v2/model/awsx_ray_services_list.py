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


class AWSXRayServicesList(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "include_all": (bool,),
            "include_only": ([str],),
        }

    attribute_map = {
        "include_all": "include_all",
        "include_only": "include_only",
    }

    def __init__(
        self_, include_all: Union[bool, UnsetType] = unset, include_only: Union[List[str], UnsetType] = unset, **kwargs
    ):
        """
        AWS X-Ray services to collect traces from

        :param include_all: Include all services
        :type include_all: bool, optional

        :param include_only: Include only these services
        :type include_only: [str], optional
        """
        if include_all is not unset:
            kwargs["include_all"] = include_all
        if include_only is not unset:
            kwargs["include_only"] = include_only
        super().__init__(kwargs)
