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


class ListRowsResponseMetaPage(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "next_continuation_token": (str,),
        }

    attribute_map = {
        "next_continuation_token": "next_continuation_token",
    }

    def __init__(self_, next_continuation_token: Union[str, UnsetType] = unset, **kwargs):
        """
        Contains the continuation token for navigating to the next page of rows.

        :param next_continuation_token: Opaque token to pass as the ``page[continuation_token]`` query parameter to fetch the next page of results. Only present when more rows are available.
        :type next_continuation_token: str, optional
        """
        if next_continuation_token is not unset:
            kwargs["next_continuation_token"] = next_continuation_token
        super().__init__(kwargs)
