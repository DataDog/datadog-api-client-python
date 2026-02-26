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
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.degradation_data_attributes_updates_items_components_affected_items import (
        DegradationDataAttributesUpdatesItemsComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
        CreateDegradationRequestDataAttributesStatus,
    )


class DegradationDataAttributesUpdatesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_data_attributes_updates_items_components_affected_items import (
            DegradationDataAttributesUpdatesItemsComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
            CreateDegradationRequestDataAttributesStatus,
        )

        return {
            "components_affected": ([DegradationDataAttributesUpdatesItemsComponentsAffectedItems],),
            "created_at": (datetime,),
            "description": (str,),
            "id": (UUID,),
            "modified_at": (datetime,),
            "started_at": (datetime,),
            "status": (CreateDegradationRequestDataAttributesStatus,),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "created_at": "created_at",
        "description": "description",
        "id": "id",
        "modified_at": "modified_at",
        "started_at": "started_at",
        "status": "status",
    }
    read_only_vars = {
        "created_at",
        "id",
        "modified_at",
    }

    def __init__(
        self_,
        components_affected: Union[
            List[DegradationDataAttributesUpdatesItemsComponentsAffectedItems], UnsetType
        ] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        id: Union[UUID, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        started_at: Union[datetime, UnsetType] = unset,
        status: Union[CreateDegradationRequestDataAttributesStatus, UnsetType] = unset,
        **kwargs,
    ):
        """


        :param components_affected: The components affected at the time of the update.
        :type components_affected: [DegradationDataAttributesUpdatesItemsComponentsAffectedItems], optional

        :param created_at: Timestamp of when the update was created.
        :type created_at: datetime, optional

        :param description: Description of the update.
        :type description: str, optional

        :param id: Identifier of the update.
        :type id: UUID, optional

        :param modified_at: Timestamp of when the update was last modified.
        :type modified_at: datetime, optional

        :param started_at: Timestamp of when the update started.
        :type started_at: datetime, optional

        :param status: The status of the degradation.
        :type status: CreateDegradationRequestDataAttributesStatus, optional
        """
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if id is not unset:
            kwargs["id"] = id
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if started_at is not unset:
            kwargs["started_at"] = started_at
        if status is not unset:
            kwargs["status"] = status
        super().__init__(kwargs)
