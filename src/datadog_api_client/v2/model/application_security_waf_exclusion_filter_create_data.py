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
    from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_attributes import (
        ApplicationSecurityWafExclusionFilterCreateAttributes,
    )
    from datadog_api_client.v2.model.application_security_waf_exclusion_filter_type import (
        ApplicationSecurityWafExclusionFilterType,
    )


class ApplicationSecurityWafExclusionFilterCreateData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_exclusion_filter_create_attributes import (
            ApplicationSecurityWafExclusionFilterCreateAttributes,
        )
        from datadog_api_client.v2.model.application_security_waf_exclusion_filter_type import (
            ApplicationSecurityWafExclusionFilterType,
        )

        return {
            "attributes": (ApplicationSecurityWafExclusionFilterCreateAttributes,),
            "type": (ApplicationSecurityWafExclusionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: ApplicationSecurityWafExclusionFilterCreateAttributes,
        type: ApplicationSecurityWafExclusionFilterType,
        **kwargs,
    ):
        """
        Object for creating a single WAF exclusion filter.

        :param attributes: Attributes for creating a WAF exclusion filter.
        :type attributes: ApplicationSecurityWafExclusionFilterCreateAttributes

        :param type: Type of the resource. The value should always be ``exclusion_filter``.
        :type type: ApplicationSecurityWafExclusionFilterType
        """
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
