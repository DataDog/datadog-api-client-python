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
    from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
        CreateConnectionRequestDataAttributesFieldsItems,
    )
    from datadog_api_client.v2.model.update_connection_request_data_attributes_fields_to_update_items import (
        UpdateConnectionRequestDataAttributesFieldsToUpdateItems,
    )


class UpdateConnectionRequestDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_connection_request_data_attributes_fields_items import (
            CreateConnectionRequestDataAttributesFieldsItems,
        )
        from datadog_api_client.v2.model.update_connection_request_data_attributes_fields_to_update_items import (
            UpdateConnectionRequestDataAttributesFieldsToUpdateItems,
        )

        return {
            "fields_to_add": ([CreateConnectionRequestDataAttributesFieldsItems],),
            "fields_to_delete": ([str],),
            "fields_to_update": ([UpdateConnectionRequestDataAttributesFieldsToUpdateItems],),
        }

    attribute_map = {
        "fields_to_add": "fields_to_add",
        "fields_to_delete": "fields_to_delete",
        "fields_to_update": "fields_to_update",
    }

    def __init__(
        self_,
        fields_to_add: Union[List[CreateConnectionRequestDataAttributesFieldsItems], UnsetType] = unset,
        fields_to_delete: Union[List[str], UnsetType] = unset,
        fields_to_update: Union[List[UpdateConnectionRequestDataAttributesFieldsToUpdateItems], UnsetType] = unset,
        **kwargs,
    ):
        """


        :param fields_to_add:
        :type fields_to_add: [CreateConnectionRequestDataAttributesFieldsItems], optional

        :param fields_to_delete:
        :type fields_to_delete: [str], optional

        :param fields_to_update:
        :type fields_to_update: [UpdateConnectionRequestDataAttributesFieldsToUpdateItems], optional
        """
        if fields_to_add is not unset:
            kwargs["fields_to_add"] = fields_to_add
        if fields_to_delete is not unset:
            kwargs["fields_to_delete"] = fields_to_delete
        if fields_to_update is not unset:
            kwargs["fields_to_update"] = fields_to_update
        super().__init__(kwargs)
