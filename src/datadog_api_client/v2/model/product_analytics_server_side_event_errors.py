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
    from datadog_api_client.v2.model.product_analytics_server_side_event_error import (
        ProductAnalyticsServerSideEventError,
    )


class ProductAnalyticsServerSideEventErrors(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.product_analytics_server_side_event_error import (
            ProductAnalyticsServerSideEventError,
        )

        return {
            "errors": ([ProductAnalyticsServerSideEventError],),
        }

    attribute_map = {
        "errors": "errors",
    }

    def __init__(self_, errors: Union[List[ProductAnalyticsServerSideEventError], UnsetType] = unset, **kwargs):
        """
        Error response.

        :param errors: Structured errors.
        :type errors: [ProductAnalyticsServerSideEventError], optional
        """
        if errors is not unset:
            kwargs["errors"] = errors
        super().__init__(kwargs)
