# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_operation_strong_link_status import RUMOperationStrongLinkStatus


class RUMOperationStrongLinkResponseAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_strong_link_status import RUMOperationStrongLinkStatus

        return {
            "created_at": (datetime,),
            "description": (str, none_type),
            "feature_id": (str,),
            "operation_id": (str,),
            "status": (RUMOperationStrongLinkStatus,),
            "tags": ([str],),
            "updated_at": (datetime, none_type),
        }

    attribute_map = {
        "created_at": "created_at",
        "description": "description",
        "feature_id": "feature_id",
        "operation_id": "operation_id",
        "status": "status",
        "tags": "tags",
        "updated_at": "updated_at",
    }
    read_only_vars = {
        "created_at",
        "feature_id",
        "operation_id",
        "updated_at",
    }

    def __init__(
        self_,
        feature_id: str,
        operation_id: str,
        status: RUMOperationStrongLinkStatus,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        updated_at: Union[datetime, none_type, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a RUM operation strong link response.

        :param created_at: The timestamp when the strong link was created.
        :type created_at: datetime, optional

        :param description: A description of the strong link.
        :type description: str, none_type, optional

        :param feature_id: The unique identifier of the linked feature.
        :type feature_id: str

        :param operation_id: The unique identifier of the linked RUM operation.
        :type operation_id: str

        :param status: The status of a RUM operation strong link.
        :type status: RUMOperationStrongLinkStatus

        :param tags: A list of tags associated with the strong link.
        :type tags: [str], optional

        :param updated_at: The timestamp when the strong link was last updated.
        :type updated_at: datetime, none_type, optional
        """
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if tags is not unset:
            kwargs["tags"] = tags
        if updated_at is not unset:
            kwargs["updated_at"] = updated_at
        super().__init__(kwargs)

        self_.feature_id = feature_id
        self_.operation_id = operation_id
        self_.status = status
