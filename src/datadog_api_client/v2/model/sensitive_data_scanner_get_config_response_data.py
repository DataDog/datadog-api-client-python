# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Any, Dict, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    date,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.sensitive_data_scanner_configuration_relationships import (
        SensitiveDataScannerConfigurationRelationships,
    )
    from datadog_api_client.v2.model.sensitive_data_scanner_configuration_type import (
        SensitiveDataScannerConfigurationType,
    )


class SensitiveDataScannerGetConfigResponseData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.sensitive_data_scanner_configuration_relationships import (
            SensitiveDataScannerConfigurationRelationships,
        )
        from datadog_api_client.v2.model.sensitive_data_scanner_configuration_type import (
            SensitiveDataScannerConfigurationType,
        )

        return {
            "attributes": (
                {
                    str: (
                        bool,
                        date,
                        datetime,
                        dict,
                        float,
                        int,
                        list,
                        str,
                        UUID,
                        none_type,
                    )
                },
            ),
            "id": (str,),
            "relationships": (SensitiveDataScannerConfigurationRelationships,),
            "type": (SensitiveDataScannerConfigurationType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "relationships": "relationships",
        "type": "type",
    }

    def __init__(
        self_,
        attributes: Union[Dict[str, Any], UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        relationships: Union[SensitiveDataScannerConfigurationRelationships, UnsetType] = unset,
        type: Union[SensitiveDataScannerConfigurationType, UnsetType] = unset,
        **kwargs,
    ):
        """
        Response data related to the scanning groups.

        :param attributes: Attributes of the Sensitive Data configuration.
        :type attributes: {str: (bool, date, datetime, dict, float, int, list, str, UUID, none_type,)}, optional

        :param id: ID of the configuration.
        :type id: str, optional

        :param relationships: Relationships of the configuration.
        :type relationships: SensitiveDataScannerConfigurationRelationships, optional

        :param type: Sensitive Data Scanner configuration type.
        :type type: SensitiveDataScannerConfigurationType, optional
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        if relationships is not unset:
            kwargs["relationships"] = relationships
        if type is not unset:
            kwargs["type"] = type
        super().__init__(kwargs)
