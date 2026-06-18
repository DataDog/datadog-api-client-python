# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.degradation_update_data_attributes_components_affected_items import (
        DegradationUpdateDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
        CreateDegradationRequestDataAttributesStatus,
    )


class DegradationUpdateDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_update_data_attributes_components_affected_items import (
            DegradationUpdateDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
            CreateDegradationRequestDataAttributesStatus,
        )

        return {
            "components_affected": ([DegradationUpdateDataAttributesComponentsAffectedItems],),
            "created_at": (datetime,),
            "deleted_at": (datetime,),
            "description": (str,),
            "modified_at": (datetime,),
            "started_at": (datetime,),
            "status": (CreateDegradationRequestDataAttributesStatus,),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "created_at": "created_at",
        "deleted_at": "deleted_at",
        "description": "description",
        "modified_at": "modified_at",
        "started_at": "started_at",
        "status": "status",
    }

    def __init__(
        self_,
        components_affected: Union[List[DegradationUpdateDataAttributesComponentsAffectedItems], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        deleted_at: Union[datetime, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        started_at: Union[datetime, UnsetType] = unset,
        status: Union[CreateDegradationRequestDataAttributesStatus, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a degradation update resource.

        :param components_affected: Components affected by this update.
        :type components_affected: [DegradationUpdateDataAttributesComponentsAffectedItems], optional

        :param created_at: The date and time the update was created.
        :type created_at: datetime, optional

        :param deleted_at: The date and time the update was soft-deleted.
        :type deleted_at: datetime, optional

        :param description: The message body of the update.
        :type description: str, optional

        :param modified_at: The date and time the update was last modified.
        :type modified_at: datetime, optional

        :param started_at: The date and time the update started.
        :type started_at: datetime, optional

        :param status: The status of the degradation.
        :type status: CreateDegradationRequestDataAttributesStatus, optional
        """
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if deleted_at is not unset:
            kwargs["deleted_at"] = deleted_at
        if description is not unset:
            kwargs["description"] = description
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
