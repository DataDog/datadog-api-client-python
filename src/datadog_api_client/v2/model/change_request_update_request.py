# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.change_request_update_data import ChangeRequestUpdateData
    from datadog_api_client.v2.model.change_request_decision_create_item import ChangeRequestDecisionCreateItem


class ChangeRequestUpdateRequest(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_update_data import ChangeRequestUpdateData
        from datadog_api_client.v2.model.change_request_decision_create_item import ChangeRequestDecisionCreateItem

        return {
            "data": (ChangeRequestUpdateData,),
            "included": ([ChangeRequestDecisionCreateItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: ChangeRequestUpdateData,
        included: Union[List[ChangeRequestDecisionCreateItem], UnsetType] = unset,
        **kwargs,
    ):
        """
        Request object to update a change request.

        :param data: Data object to update a change request.
        :type data: ChangeRequestUpdateData

        :param included: Included resources for the change request update.
        :type included: [ChangeRequestDecisionCreateItem], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
