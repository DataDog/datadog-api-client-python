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
    from datadog_api_client.v2.model.degradation_update_data import DegradationUpdateData
    from datadog_api_client.v2.model.degradation_update_included import DegradationUpdateIncluded
    from datadog_api_client.v2.model.status_pages_user import StatusPagesUser
    from datadog_api_client.v2.model.degradation import Degradation
    from datadog_api_client.v2.model.status_page_as_included import StatusPageAsIncluded


class DegradationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_update_data import DegradationUpdateData
        from datadog_api_client.v2.model.degradation_update_included import DegradationUpdateIncluded

        return {
            "data": (DegradationUpdateData,),
            "included": ([DegradationUpdateIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: Union[DegradationUpdateData, UnsetType] = unset,
        included: Union[
            List[Union[DegradationUpdateIncluded, StatusPagesUser, Degradation, StatusPageAsIncluded]], UnsetType
        ] = unset,
        **kwargs,
    ):
        """
        Response object for a degradation update.

        :param data: The data object for a degradation update.
        :type data: DegradationUpdateData, optional

        :param included: Resources related to the degradation update.
        :type included: [DegradationUpdateIncluded], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
