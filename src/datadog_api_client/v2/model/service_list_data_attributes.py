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
    from datadog_api_client.v2.model.service_list_data_attributes_metadata_items import (
        ServiceListDataAttributesMetadataItems,
    )


class ServiceListDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.service_list_data_attributes_metadata_items import (
            ServiceListDataAttributesMetadataItems,
        )

        return {
            "metadata": ([ServiceListDataAttributesMetadataItems],),
            "services": ([str],),
        }

    attribute_map = {
        "metadata": "metadata",
        "services": "services",
    }

    def __init__(
        self_,
        metadata: Union[List[ServiceListDataAttributesMetadataItems], UnsetType] = unset,
        services: Union[List[str], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param metadata:
        :type metadata: [ServiceListDataAttributesMetadataItems], optional

        :param services:
        :type services: [str], optional
        """
        if metadata is not unset:
            kwargs["metadata"] = metadata
        if services is not unset:
            kwargs["services"] = services
        super().__init__(kwargs)
