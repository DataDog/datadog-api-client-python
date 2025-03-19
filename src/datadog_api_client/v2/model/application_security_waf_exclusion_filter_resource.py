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
    from datadog_api_client.v2.model.application_security_waf_exclusion_filter_attributes import (
        ApplicationSecurityWafExclusionFilterAttributes,
    )
    from datadog_api_client.v2.model.application_security_waf_exclusion_filter_type import (
        ApplicationSecurityWafExclusionFilterType,
    )


class ApplicationSecurityWafExclusionFilterResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_waf_exclusion_filter_attributes import (
            ApplicationSecurityWafExclusionFilterAttributes,
        )
        from datadog_api_client.v2.model.application_security_waf_exclusion_filter_type import (
            ApplicationSecurityWafExclusionFilterType,
        )

        return {
            "attributes": (ApplicationSecurityWafExclusionFilterAttributes,),
            "id": (str,),
            "type": (ApplicationSecurityWafExclusionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }
    read_only_vars = {
        "id",
    }

    def __init__(
        self_,
        attributes: Union[ApplicationSecurityWafExclusionFilterAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        type: Union[ApplicationSecurityWafExclusionFilterType, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON:API resource for an WAF exclusion filter.

        :param attributes: Attributes describing a WAF exclusion filter.
        :type attributes: ApplicationSecurityWafExclusionFilterAttributes, optional

        :param id: The identifier of the WAF exclusion filter.
        :type id: str, optional

        :param type: Type of the resource. The value should always be ``exclusion_filter``.
        :type type: ApplicationSecurityWafExclusionFilterType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
