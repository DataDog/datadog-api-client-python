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
    from datadog_api_client.v2.model.application_security_exclusion_filter_attributes import (
        ApplicationSecurityExclusionFilterAttributes,
    )
    from datadog_api_client.v2.model.application_security_exclusion_filter_metadata import (
        ApplicationSecurityExclusionFilterMetadata,
    )
    from datadog_api_client.v2.model.application_security_exclusion_filter_type import (
        ApplicationSecurityExclusionFilterType,
    )


class ApplicationSecurityExclusionFilterResource(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.application_security_exclusion_filter_attributes import (
            ApplicationSecurityExclusionFilterAttributes,
        )
        from datadog_api_client.v2.model.application_security_exclusion_filter_metadata import (
            ApplicationSecurityExclusionFilterMetadata,
        )
        from datadog_api_client.v2.model.application_security_exclusion_filter_type import (
            ApplicationSecurityExclusionFilterType,
        )

        return {
            "attributes": (ApplicationSecurityExclusionFilterAttributes,),
            "id": (str,),
            "meta": (ApplicationSecurityExclusionFilterMetadata,),
            "type": (ApplicationSecurityExclusionFilterType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "meta": "meta",
        "type": "type",
    }
    read_only_vars = {
        "id",
        "meta",
    }

    def __init__(
        self_,
        attributes: ApplicationSecurityExclusionFilterAttributes,
        type: ApplicationSecurityExclusionFilterType,
        id: Union[str, UnsetType] = unset,
        meta: Union[ApplicationSecurityExclusionFilterMetadata, UnsetType] = unset,
        **kwargs,
    ):
        """
        A JSON:API resource for an Application Security exclusion filter.

        :param attributes: Attributes describing an Application Security exclusion filter.
        :type attributes: ApplicationSecurityExclusionFilterAttributes

        :param id: The identifier of the exclusion filter.
        :type id: str, optional

        :param meta: Extra information about the exclusion filter.
        :type meta: ApplicationSecurityExclusionFilterMetadata, optional

        :param type: Type of the resource. The value should always be ``exclusion_filter``.
        :type type: ApplicationSecurityExclusionFilterType
        """
        if id is not unset:
            kwargs["id"] = id
        if meta is not unset:
            kwargs["meta"] = meta
        super().__init__(kwargs)

        self_.attributes = attributes
        self_.type = type
