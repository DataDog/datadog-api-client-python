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
    from datadog_api_client.v2.model.ci_app_test_query_page_limit import CIAppTestQueryPageLimit


class CIAppTestQueryPageOptions(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.ci_app_test_query_page_limit import CIAppTestQueryPageLimit

        return {
            "cursor": (str,),
            "limit": (CIAppTestQueryPageLimit,),
        }

    attribute_map = {
        "cursor": "cursor",
        "limit": "limit",
    }

    def __init__(
        self_,
        cursor: Union[str, UnsetType] = unset,
        limit: Union[CIAppTestQueryPageLimit, int, str, UnsetType] = unset,
        **kwargs,
    ):
        """
        Paging attributes for listing test events.

        :param cursor: List following results with a cursor provided in the previous query.
        :type cursor: str, optional

        :param limit: Maximum number of events in the response, supplied as an integer or a string containing decimal digits.
        :type limit: CIAppTestQueryPageLimit, optional
        """
        if cursor is not unset:
            kwargs["cursor"] = cursor
        if limit is not unset:
            kwargs["limit"] = limit
        super().__init__(kwargs)
