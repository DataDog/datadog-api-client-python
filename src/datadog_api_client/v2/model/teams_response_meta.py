# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.teams_response_meta_pagination import TeamsResponseMetaPagination


class TeamsResponseMeta(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.teams_response_meta_pagination import TeamsResponseMetaPagination

        return {
            "pagination": (TeamsResponseMetaPagination,),
        }

    attribute_map = {
        "pagination": "pagination",
    }

    def __init__(self_, pagination: Union[TeamsResponseMetaPagination, UnsetType] = unset, **kwargs):
        """
        Teams response metadata.

        :param pagination: Teams response metadata.
        :type pagination: TeamsResponseMetaPagination, optional
        """
        if pagination is not unset:
            kwargs["pagination"] = pagination
        super().__init__(kwargs)
