# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


class DataDeletionResponseItemAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        return {
            "created_at": (str,),
            "created_by": (str,),
            "from_time": (int,),
            "indexes": ([str],),
            "is_created": (bool,),
            "org_id": (int,),
            "product": (str,),
            "query": (str,),
            "starting_at": (str,),
            "status": (str,),
            "to_time": (int,),
            "total_unrestricted": (int,),
            "updated_at": (str,),
        }

    attribute_map = {
        "created_at": "created_at",
        "created_by": "created_by",
        "from_time": "from_time",
        "indexes": "indexes",
        "is_created": "is_created",
        "org_id": "org_id",
        "product": "product",
        "query": "query",
        "starting_at": "starting_at",
        "status": "status",
        "to_time": "to_time",
        "total_unrestricted": "total_unrestricted",
        "updated_at": "updated_at",
    }

    def __init__(
        self_,
        created_at: str,
        created_by: str,
        from_time: int,
        is_created: bool,
        org_id: int,
        product: str,
        query: str,
        starting_at: str,
        status: str,
        to_time: int,
        total_unrestricted: int,
        updated_at: str,
        indexes: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Deletion attribute for data deletion response.

        :param created_at: Creation time of the deletion request.
        :type created_at: str

        :param created_by: User who created the deletion request.
        :type created_by: str

        :param from_time: Start of requested time window, milliseconds since Unix epoch.
        :type from_time: int

        :param indexes: List of indexes for the search. If not provided, the search is performed in all indexes.
        :type indexes: [str], optional

        :param is_created: Whether the deletion request is fully created or not. It can take several minutes to fully create a deletion request depending on the target query and timeframe.
        :type is_created: bool

        :param org_id: Organization ID.
        :type org_id: int

        :param product: Product name.
        :type product: str

        :param query: Query for creating a data deletion request.
        :type query: str

        :param starting_at: Starting time of the process to delete the requested data.
        :type starting_at: str

        :param status: Status of the deletion request.
        :type status: str

        :param to_time: End of requested time window, milliseconds since Unix epoch.
        :type to_time: int

        :param total_unrestricted: Total number of elements to be deleted. Only the data accessible to the current user that matches the query and timeframe provided will be deleted.
        :type total_unrestricted: int

        :param updated_at: Update time of the deletion request.
        :type updated_at: str
        """
        if indexes is not unset:
            kwargs["indexes"] = indexes
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.created_by = created_by
        self_.from_time = from_time
        self_.is_created = is_created
        self_.org_id = org_id
        self_.product = product
        self_.query = query
        self_.starting_at = starting_at
        self_.status = status
        self_.to_time = to_time
        self_.total_unrestricted = total_unrestricted
        self_.updated_at = updated_at
