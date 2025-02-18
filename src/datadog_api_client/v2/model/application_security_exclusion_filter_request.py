# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.application_security_exclusion_filter_resource import (
        ApplicationSecurityExclusionFilterResource,
    )


class ApplicationSecurityExclusionFilterRequest(ModelNormal):
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

    def __init__(self_, data: ApplicationSecurityExclusionFilterResource, **kwargs):
        """
        Request object for a single Application Security exclusion filter.

        :param data: A JSON:API resource for an Application Security exclusion filter.
        :type data: ApplicationSecurityExclusionFilterResource
        """
        super().__init__(kwargs)

        self_.data = data
