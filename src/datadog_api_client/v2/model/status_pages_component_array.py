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
    from datadog_api_client.v2.model.status_pages_component_data import StatusPagesComponentData
    from datadog_api_client.v2.model.status_pages_component_array_included import StatusPagesComponentArrayIncluded
    from datadog_api_client.v2.model.status_pages_user import StatusPagesUser
    from datadog_api_client.v2.model.status_page_as_included import StatusPageAsIncluded
    from datadog_api_client.v2.model.status_pages_component_group import StatusPagesComponentGroup


class StatusPagesComponentArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.status_pages_component_data import StatusPagesComponentData
        from datadog_api_client.v2.model.status_pages_component_array_included import StatusPagesComponentArrayIncluded

        return {
            "data": ([StatusPagesComponentData],),
            "included": ([StatusPagesComponentArrayIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[StatusPagesComponentData],
        included: Union[
            List[
                Union[
                    StatusPagesComponentArrayIncluded, StatusPagesUser, StatusPageAsIncluded, StatusPagesComponentGroup
                ]
            ],
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """


        :param data:
        :type data: [StatusPagesComponentData]

        :param included: The included related resources of a component. Client must explicitly request these resources by name in the ``include`` query parameter.
        :type included: [StatusPagesComponentArrayIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
