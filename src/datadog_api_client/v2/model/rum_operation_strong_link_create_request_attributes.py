# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.rum_operation_strong_link_status import RUMOperationStrongLinkStatus


class RUMOperationStrongLinkCreateRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_strong_link_status import RUMOperationStrongLinkStatus

        return {
            "application_id": (UUID,),
            "description": (str, none_type),
            "feature_id": (str,),
            "operation_id": (str,),
            "operation_name": (str,),
            "status": (RUMOperationStrongLinkStatus,),
            "tags": ([str],),
        }

    attribute_map = {
        "application_id": "application_id",
        "description": "description",
        "feature_id": "feature_id",
        "operation_id": "operation_id",
        "operation_name": "operation_name",
        "status": "status",
        "tags": "tags",
    }

    def __init__(
        self_,
        feature_id: str,
        application_id: Union[UUID, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        operation_id: Union[str, UnsetType] = unset,
        operation_name: Union[str, UnsetType] = unset,
        status: Union[RUMOperationStrongLinkStatus, UnsetType] = unset,
        tags: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating a RUM operation strong link.

        :param application_id: The RUM application ID used when creating a stub operation from ``operation_name``.
        :type application_id: UUID, optional

        :param description: A description of the strong link.
        :type description: str, none_type, optional

        :param feature_id: The unique identifier of the feature to link.
        :type feature_id: str

        :param operation_id: The unique identifier of the RUM operation to link. Either ``operation_id`` or
            ``operation_name`` is required.
        :type operation_id: str, optional

        :param operation_name: The name of the RUM operation to link. Either ``operation_id`` or ``operation_name`` is
            required. If no operation with this name exists, a stub operation is created.
        :type operation_name: str, optional

        :param status: The status of a RUM operation strong link.
        :type status: RUMOperationStrongLinkStatus, optional

        :param tags: A list of tags associated with the strong link.
        :type tags: [str], optional
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if description is not unset:
            kwargs["description"] = description
        if operation_id is not unset:
            kwargs["operation_id"] = operation_id
        if operation_name is not unset:
            kwargs["operation_name"] = operation_name
        if status is not unset:
            kwargs["status"] = status
        if tags is not unset:
            kwargs["tags"] = tags
        super().__init__(kwargs)

        self_.feature_id = feature_id
