# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import List, Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    none_type,
    unset,
    UnsetType,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.any_value import AnyValue
    from datadog_api_client.v2.model.any_value_object import AnyValueObject
    from datadog_api_client.v2.model.any_value_item import AnyValueItem


class IntegrationJiraSyncPropertiesCustomFieldsAdditionalProperties(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.any_value import AnyValue

        return {
            "sync_type": (str,),
            "value": (AnyValue,),
        }

    attribute_map = {
        "sync_type": "sync_type",
        "value": "value",
    }

    def __init__(
        self_,
        sync_type: Union[str, UnsetType] = unset,
        value: Union[
            Union[
                AnyValue, str, float, AnyValueObject, List[Union[AnyValueItem, str, float, AnyValueObject, bool]], bool
            ],
            none_type,
            UnsetType,
        ] = unset,
        **kwargs,
    ):
        """


        :param sync_type:
        :type sync_type: str, optional

        :param value: Represents any valid JSON value.
        :type value: AnyValue, none_type, optional
        """
        if sync_type is not unset:
            kwargs["sync_type"] = sync_type
        if value is not unset:
            kwargs["value"] = value
        super().__init__(kwargs)
