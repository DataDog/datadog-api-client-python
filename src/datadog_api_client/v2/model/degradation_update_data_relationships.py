# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.degradation_update_data_relationships_user import (
        DegradationUpdateDataRelationshipsUser,
    )
    from datadog_api_client.v2.model.degradation_update_data_relationships_degradation import (
        DegradationUpdateDataRelationshipsDegradation,
    )
    from datadog_api_client.v2.model.degradation_update_data_relationships_status_page import (
        DegradationUpdateDataRelationshipsStatusPage,
    )


class DegradationUpdateDataRelationships(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_update_data_relationships_user import (
            DegradationUpdateDataRelationshipsUser,
        )
        from datadog_api_client.v2.model.degradation_update_data_relationships_degradation import (
            DegradationUpdateDataRelationshipsDegradation,
        )
        from datadog_api_client.v2.model.degradation_update_data_relationships_status_page import (
            DegradationUpdateDataRelationshipsStatusPage,
        )

        return {
            "created_by_user": (DegradationUpdateDataRelationshipsUser,),
            "degradation": (DegradationUpdateDataRelationshipsDegradation,),
            "deleted_by_user": (DegradationUpdateDataRelationshipsUser,),
            "last_modified_by_user": (DegradationUpdateDataRelationshipsUser,),
            "status_page": (DegradationUpdateDataRelationshipsStatusPage,),
        }

    attribute_map = {
        "created_by_user": "created_by_user",
        "degradation": "degradation",
        "deleted_by_user": "deleted_by_user",
        "last_modified_by_user": "last_modified_by_user",
        "status_page": "status_page",
    }

    def __init__(
        self_,
        created_by_user: Union[DegradationUpdateDataRelationshipsUser, UnsetType] = unset,
        degradation: Union[DegradationUpdateDataRelationshipsDegradation, UnsetType] = unset,
        deleted_by_user: Union[DegradationUpdateDataRelationshipsUser, UnsetType] = unset,
        last_modified_by_user: Union[DegradationUpdateDataRelationshipsUser, UnsetType] = unset,
        status_page: Union[DegradationUpdateDataRelationshipsStatusPage, UnsetType] = unset,
        **kwargs,
    ):
        """
        Relationships of a degradation update resource.

        :param created_by_user: A user relationship of a degradation update.
        :type created_by_user: DegradationUpdateDataRelationshipsUser, optional

        :param degradation: The degradation relationship of a degradation update.
        :type degradation: DegradationUpdateDataRelationshipsDegradation, optional

        :param deleted_by_user: A user relationship of a degradation update.
        :type deleted_by_user: DegradationUpdateDataRelationshipsUser, optional

        :param last_modified_by_user: A user relationship of a degradation update.
        :type last_modified_by_user: DegradationUpdateDataRelationshipsUser, optional

        :param status_page: The status page relationship of a degradation update.
        :type status_page: DegradationUpdateDataRelationshipsStatusPage, optional
        """
        if created_by_user is not unset:
            kwargs["created_by_user"] = created_by_user
        if degradation is not unset:
            kwargs["degradation"] = degradation
        if deleted_by_user is not unset:
            kwargs["deleted_by_user"] = deleted_by_user
        if last_modified_by_user is not unset:
            kwargs["last_modified_by_user"] = last_modified_by_user
        if status_page is not unset:
            kwargs["status_page"] = status_page
        super().__init__(kwargs)
