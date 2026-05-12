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
    from datadog_api_client.v2.model.create_degradation_request_data_attributes_components_affected_items import (
        CreateDegradationRequestDataAttributesComponentsAffectedItems,
    )
    from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
        CreateDegradationRequestDataAttributesStatus,
    )


class CreateBackfilledDegradationRequestDataAttributesUpdatesItems(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_degradation_request_data_attributes_components_affected_items import (
            CreateDegradationRequestDataAttributesComponentsAffectedItems,
        )
        from datadog_api_client.v2.model.create_degradation_request_data_attributes_status import (
            CreateDegradationRequestDataAttributesStatus,
        )

        return {
            "components_affected": ([CreateDegradationRequestDataAttributesComponentsAffectedItems],),
            "description": (str,),
            "started_at": (datetime,),
            "status": (CreateDegradationRequestDataAttributesStatus,),
        }

    attribute_map = {
        "components_affected": "components_affected",
        "description": "description",
        "started_at": "started_at",
        "status": "status",
    }

    def __init__(
        self_,
        started_at: datetime,
        status: CreateDegradationRequestDataAttributesStatus,
        components_affected: Union[
            List[CreateDegradationRequestDataAttributesComponentsAffectedItems], UnsetType
        ] = unset,
        description: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        A backfilled degradation update entry.

        :param components_affected: The components affected.
        :type components_affected: [CreateDegradationRequestDataAttributesComponentsAffectedItems], optional

        :param description: A description of the update.
        :type description: str, optional

        :param started_at: Timestamp of when the update occurred.
        :type started_at: datetime

        :param status: The status of the degradation.
        :type status: CreateDegradationRequestDataAttributesStatus
        """
        if components_affected is not unset:
            kwargs["components_affected"] = components_affected
        if description is not unset:
            kwargs["description"] = description
        super().__init__(kwargs)

        self_.started_at = started_at
        self_.status = status
