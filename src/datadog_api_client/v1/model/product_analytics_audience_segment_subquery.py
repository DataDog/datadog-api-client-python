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


class ProductAnalyticsAudienceSegmentSubquery(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "name": (str,),
            "segment_id": (str,),
        }

    attribute_map = {
        "name": "name",
        "segment_id": "segment_id",
    }

    def __init__(self_, name: Union[str, UnsetType] = unset, segment_id: Union[str, UnsetType] = unset, **kwargs):
        """
        Product Analytics audience segment subquery.

        :param name:
        :type name: str, optional

        :param segment_id:
        :type segment_id: str, optional
        """
        if name is not unset:
            kwargs["name"] = name
        if segment_id is not unset:
            kwargs["segment_id"] = segment_id
        super().__init__(kwargs)
