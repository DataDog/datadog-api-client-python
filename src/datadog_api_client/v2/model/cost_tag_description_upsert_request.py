# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.cost_tag_description_upsert_request_data import CostTagDescriptionUpsertRequestData


class CostTagDescriptionUpsertRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.cost_tag_description_upsert_request_data import (
            CostTagDescriptionUpsertRequestData,
        )

        return {
            "data": (CostTagDescriptionUpsertRequestData,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: CostTagDescriptionUpsertRequestData, **kwargs):
        """
        Request body for creating or updating a Cloud Cost Management tag key description.

        :param data: Resource envelope carrying the tag key description being upserted. The ``id`` is informational; the authoritative tag key is taken from the URL path.
        :type data: CostTagDescriptionUpsertRequestData
        """
        super().__init__(kwargs)

        self_.data = data
