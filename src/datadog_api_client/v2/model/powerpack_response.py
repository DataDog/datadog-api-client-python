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
    from datadog_api_client.v2.model.powerpack_data import PowerpackData
    from datadog_api_client.v2.model.user import User


class PowerpackResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.powerpack_data import PowerpackData
        from datadog_api_client.v2.model.user import User

        return {
            "data": (PowerpackData,),
            "included": ([User],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_, data: Union[PowerpackData, UnsetType] = unset, included: Union[List[User], UnsetType] = unset, **kwargs
    ):
        """
        Response object which includes a single powerpack configuration.

        :param data: Powerpack data object.
        :type data: PowerpackData, optional

        :param included: Array of objects related to the users.
        :type included: [User], optional
        """
        if data is not unset:
            kwargs["data"] = data
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)
