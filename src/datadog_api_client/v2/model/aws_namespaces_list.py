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


class AWSNamespacesList(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "exclude_all": (bool,),
            "exclude_only": ([str],),
            "include_all": (bool,),
            "include_only": ([str],),
        }

    attribute_map = {
        "exclude_all": "exclude_all",
        "exclude_only": "exclude_only",
        "include_all": "include_all",
        "include_only": "include_only",
    }

    def __init__(
        self_,
        exclude_all: Union[bool, UnsetType] = unset,
        exclude_only: Union[List[str], UnsetType] = unset,
        include_all: Union[bool, UnsetType] = unset,
        include_only: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        AWS Metrics namespace filters

        :param exclude_all: Exclude all namespaces
        :type exclude_all: bool, optional

        :param exclude_only: Exclude only these namespaces
        :type exclude_only: [str], optional

        :param include_all: Include all namespaces
        :type include_all: bool, optional

        :param include_only: Include only these namespaces
        :type include_only: [str], optional
        """
        if exclude_all is not unset:
            kwargs["exclude_all"] = exclude_all
        if exclude_only is not unset:
            kwargs["exclude_only"] = exclude_only
        if include_all is not unset:
            kwargs["include_all"] = include_all
        if include_only is not unset:
            kwargs["include_only"] = include_only
        super().__init__(kwargs)
