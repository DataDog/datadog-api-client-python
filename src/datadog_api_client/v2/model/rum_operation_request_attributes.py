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
    from datadog_api_client.v2.model.rum_operation_journey_rum import RUMOperationJourneyRum


class RUMOperationRequestAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_operation_journey_rum import RUMOperationJourneyRum

        return {
            "application_id": (UUID, none_type),
            "category": (str, none_type),
            "description": (str, none_type),
            "display_name": (str,),
            "feature_ids": ([str],),
            "journey_rum": (RUMOperationJourneyRum,),
            "name": (str,),
            "tags": ([str],),
        }

    attribute_map = {
        "application_id": "application_id",
        "category": "category",
        "description": "description",
        "display_name": "display_name",
        "feature_ids": "feature_ids",
        "journey_rum": "journey_rum",
        "name": "name",
        "tags": "tags",
    }

    def __init__(
        self_,
        journey_rum: RUMOperationJourneyRum,
        name: str,
        tags: List[str],
        application_id: Union[UUID, none_type, UnsetType] = unset,
        category: Union[str, none_type, UnsetType] = unset,
        description: Union[str, none_type, UnsetType] = unset,
        display_name: Union[str, UnsetType] = unset,
        feature_ids: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes for creating or updating a RUM operation.

        :param application_id: The RUM application ID the operation belongs to.
        :type application_id: UUID, none_type, optional

        :param category: The category of the RUM operation.
        :type category: str, none_type, optional

        :param description: A description of the RUM operation.
        :type description: str, none_type, optional

        :param display_name: A human-readable display name for the RUM operation.
        :type display_name: str, optional

        :param feature_ids: The list of feature IDs associated with the RUM operation.
        :type feature_ids: [str], optional

        :param journey_rum: The definition of a RUM operation's journey, used to detect it from RUM events.
        :type journey_rum: RUMOperationJourneyRum

        :param name: The unique name of the RUM operation. Must not contain spaces.
        :type name: str

        :param tags: A list of tags associated with the RUM operation.
        :type tags: [str]
        """
        if application_id is not unset:
            kwargs["application_id"] = application_id
        if category is not unset:
            kwargs["category"] = category
        if description is not unset:
            kwargs["description"] = description
        if display_name is not unset:
            kwargs["display_name"] = display_name
        if feature_ids is not unset:
            kwargs["feature_ids"] = feature_ids
        super().__init__(kwargs)

        self_.journey_rum = journey_rum
        self_.name = name
        self_.tags = tags
