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
    from datadog_api_client.v2.model.application_security_exclusion_filter_resource import (
        ApplicationSecurityExclusionFilterResource,
    )


class ApplicationSecurityExclusionFilterResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_exclusion_filter_resource import (
            ApplicationSecurityExclusionFilterResource,
        )

        return {
            "data": (ApplicationSecurityExclusionFilterResource,),
        }

    attribute_map = {
        "data": "data",
    }

    def __init__(self_, data: Union[ApplicationSecurityExclusionFilterResource, UnsetType] = unset, **kwargs):
        """
        Response object for a single Application Security exclusion filter.

        :param data: A JSON:API resource for an Application Security exclusion filter.
        :type data: ApplicationSecurityExclusionFilterResource, optional
        """
        if data is not unset:
            kwargs["data"] = data
        super().__init__(kwargs)
