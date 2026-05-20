# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class LLMObsDataDeletionResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (datetime,),
            "created_by": (str,),
            "from_time": (int,),
            "org_id": (int,),
            "product": (str,),
            "query": (str,),
            "to_time": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "from_time": "from_time",
        "org_id": "org_id",
        "product": "product",
        "query": "query",
        "to_time": "to_time",
    }

    def __init__(
        self_,
        created_at: datetime,
        created_by: str,
        from_time: int,
        org_id: int,
        product: str,
        query: str,
        to_time: int,
        **kwargs,
    ):
        """
        Attributes of a submitted LLM Observability data deletion request.

        :param created_at: Timestamp when the deletion request was created.
        :type created_at: datetime

        :param created_by: UUID of the user who created the deletion request.
        :type created_by: str

        :param from_time: Start of the deletion time range in milliseconds since Unix epoch.
        :type from_time: int

        :param org_id: ID of the organization that submitted the deletion request.
        :type org_id: int

        :param product: Product name for the deletion request.
        :type product: str

        :param query: The query string used to select data for deletion.
        :type query: str

        :param to_time: End of the deletion time range in milliseconds since Unix epoch.
        :type to_time: int
        """
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.from_time = from_time
        self_.org_id = org_id
        self_.product = product
        self_.query = query
        self_.to_time = to_time
