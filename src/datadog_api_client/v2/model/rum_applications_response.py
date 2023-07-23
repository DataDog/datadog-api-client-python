# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from dataclasses import dataclass
from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_application_list import RUMApplicationList


@dataclass
class RUMApplicationsResponseJSON:
    type: str
    application_id: Union[str, UnsetType] = unset
    created_at: Union[int, UnsetType] = unset
    created_by_handle: Union[str, UnsetType] = unset
    hash: Union[str, UnsetType] = unset
    is_active: Union[bool, UnsetType] = unset
    name: Union[str, UnsetType] = unset
    org_id: Union[int, UnsetType] = unset
    updated_at: Union[int, UnsetType] = unset
    updated_by_handle: Union[str, UnsetType] = unset


class RUMApplicationsResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_application_list import RUMApplicationList

        return {
            "data": ([RUMApplicationList],),
        }

    attribute_map = {
        "data": "data",
    }
    json_api_model = RUMApplicationsResponseJSON

    def __init__(self_, data: Union[List[RUMApplicationList], UnsetType] = unset, **kwargs):
        """
        RUM applications response.

        :param data: RUM applications array response.
        :type data: [RUMApplicationList], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
