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
    from datadog_api_client.v2.model.change_request_response_data import ChangeRequestResponseData
    from datadog_api_client.v2.model.change_request_included_item import ChangeRequestIncludedItem
    from datadog_api_client.v2.model.change_request_included_user import ChangeRequestIncludedUser
    from datadog_api_client.v2.model.change_request_included_decision import ChangeRequestIncludedDecision


class ChangeRequestResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.change_request_response_data import ChangeRequestResponseData
        from datadog_api_client.v2.model.change_request_included_item import ChangeRequestIncludedItem

        return {
            "data": (ChangeRequestResponseData,),
            "included": ([ChangeRequestIncludedItem],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: ChangeRequestResponseData,
        included: Union[
            List[Union[ChangeRequestIncludedItem, ChangeRequestIncludedUser, ChangeRequestIncludedDecision]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Response object for a change request.

        :param data: Data object for a change request response.
        :type data: ChangeRequestResponseData

        :param included: Included resources related to the change request.
        :type included: [ChangeRequestIncludedItem], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
