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
    from datadog_api_client.v2.model.degradation_template_data import DegradationTemplateData
    from datadog_api_client.v2.model.degradation_included import DegradationIncluded
    from datadog_api_client.v2.model.status_pages_user import StatusPagesUser
    from datadog_api_client.v2.model.status_page_as_included import StatusPageAsIncluded


class DegradationTemplateArray(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.degradation_template_data import DegradationTemplateData
        from datadog_api_client.v2.model.degradation_included import DegradationIncluded

        return {
            "data": ([DegradationTemplateData],),
            "included": ([DegradationIncluded],),
        }

    attribute_map = {
        "data": "data",
        "included": "included",
    }

    def __init__(
        self_,
        data: List[DegradationTemplateData],
        included: Union[List[Union[DegradationIncluded, StatusPagesUser, StatusPageAsIncluded]], UnsetType] = unset,
        **kwargs,
    ):
        """
        Response object for a list of degradation templates.

        :param data: A list of degradation template data objects.
        :type data: [DegradationTemplateData]

        :param included: The included related resources of a degradation template. Client must explicitly request these resources by name in the ``include`` query parameter.
        :type included: [DegradationIncluded], optional
        """
        if included is not unset:
            kwargs["included"] = included
        super().__init__(kwargs)

        self_.data = data
