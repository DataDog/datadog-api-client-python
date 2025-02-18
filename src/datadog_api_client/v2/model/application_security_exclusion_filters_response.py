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
    from datadog_api_client.v2.model.application_security_exclusion_filter_resource import (
        ApplicationSecurityExclusionFilterResource,
    )


class ApplicationSecurityExclusionFiltersResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_exclusion_filter_resource import (
            ApplicationSecurityExclusionFilterResource,
        )

        return {
            "data": ([ApplicationSecurityExclusionFilterResource],),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[List[ApplicationSecurityExclusionFilterResource], UnsetType] = unset, **kwargs):
        """
        Response object for multiple Application Security exclusion filters.

        :param data: A list of Application Security exclusion filter.
        :type data: [ApplicationSecurityExclusionFilterResource], optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
