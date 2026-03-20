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
    from datadog_api_client.v2.model.environment import Environment
    from datadog_api_client.v2.model.environments_pagination_meta import EnvironmentsPaginationMeta


class ListEnvironmentsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.environment import Environment
        from datadog_api_client.v2.model.environments_pagination_meta import EnvironmentsPaginationMeta

        return {
            "data": ([Environment],),
            "meta": (EnvironmentsPaginationMeta,),
        }

    attribute_map = {
        "data": "data",
        "meta": "meta",
    }

    def __init__(self_, data: List[Environment], meta: Union[EnvironmentsPaginationMeta, UnsetType] = unset, **kwargs):
        """
        Response containing a list of environments.

        :param data: List of environments.
        :type data: [Environment]

        :param meta: Pagination metadata for environments.
        :type meta: EnvironmentsPaginationMeta, optional
        """
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.data = data
