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


class FormVersionUpsertParams(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "etag": (str,),
            "match_policy": (str,),
        }

    attribute_map = {
        "etag": "etag",
        "match_policy": "match_policy",
    }

    def __init__(self_, etag: Union[str, UnsetType] = unset, match_policy: Union[str, UnsetType] = unset, **kwargs):
        """
        Parameters for upserting a form version.

        :param etag: The entity tag for conflict detection.
        :type etag: str, optional

        :param match_policy: The match policy for upserting.
        :type match_policy: str, optional
        """
        if etag is not unset:
            kwargs["etag"] = etag
        if match_policy is not unset:
            kwargs["match_policy"] = match_policy
        super().__init__(kwargs)
