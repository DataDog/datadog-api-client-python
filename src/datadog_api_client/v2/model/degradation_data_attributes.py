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
    from datadog_api_client.v2.model.degradation_data_attributes_components_affected_items import (
        DegradationDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
        CreateDegradationRequestDataAttributesStatus,
    )
    from datadog_api_client.v2.model.degradation_data_attributes_updates_items import (
        DegradationDataAttributesUpdatesItems,
    )


class DegradationDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_data_attributes_components_affected_items import (
            DegradationDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
            CreateDegradationRequestDataAttributesStatus,
        )
        from datadog_api_client.v2.model.degradation_data_attributes_updates_items import (
            DegradationDataAttributesUpdatesItems,
        )

        return {
            "components_affected": ([DegradationDataAttributesComponentsAffectedItems],),
            "created_at": (datetime,),
            "description": (str,),
            "modified_at": (datetime,),
            "status": (CreateDegradationRequestDataAttributesStatus,),
            "title": (str,),
            "updates": ([DegradationDataAttributesUpdatesItems],),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "created_at": "created_at",
        "description": "description",
        "modified_at": "modified_at",
        "status": "status",
        "title": "title",
        "updates": "updates",
    }

    def __init__(
        self_,
        components_affected: Union[List[DegradationDataAttributesComponentsAffectedItems], UnsetType] = unset,
        created_at: Union[datetime, UnsetType] = unset,
        description: Union[str, UnsetType] = unset,
        modified_at: Union[datetime, UnsetType] = unset,
        status: Union[CreateDegradationRequestDataAttributesStatus, UnsetType] = unset,
        title: Union[str, UnsetType] = unset,
        updates: Union[List[DegradationDataAttributesUpdatesItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param components_affected:
        :type components_affected: [DegradationDataAttributesComponentsAffectedItems], optional

        :param created_at:
        :type created_at: datetime, optional

        :param description:
        :type description: str, optional

        :param modified_at:
        :type modified_at: datetime, optional

        :param status:
        :type status: CreateDegradationRequestDataAttributesStatus, optional

        :param title:
        :type title: str, optional

        :param updates:
        :type updates: [DegradationDataAttributesUpdatesItems], optional
        """
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if created_at is not unset:
            kwargs["created_at"] = created_at
        if description is not unset:
            kwargs["description"] = description
        if modified_at is not unset:
            kwargs["modified_at"] = modified_at
        if status is not unset:
            kwargs["status"] = status
        if title is not unset:
            kwargs["title"] = title
        if updates is not unset:
            kwargs["updates"] = updates
        super().__init__(kwargs)
