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
    from datadog_api_client.v2.model.restriction_query_create_data import RestrictionQueryCreateData


class RestrictionQueryCreatePayload(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.restriction_query_create_data import RestrictionQueryCreateData

        return {
            "data": (RestrictionQueryCreateData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[RestrictionQueryCreateData, UnsetType] = unset, **kwargs):
        """
        Create a restriction query.

        :param data: Data related to the creation of a restriction query.
        :type data: RestrictionQueryCreateData, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
