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
    from datadog_api_client.v2.model.update_apps_datastore_request_data_attributes import (
        UpdateAppsDatastoreRequestDataAttributes,
    )
    from datadog_api_client.v2.model.update_apps_datastore_request_data_type import UpdateAppsDatastoreRequestDataType


class UpdateAppsDatastoreRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.update_apps_datastore_request_data_attributes import (
            UpdateAppsDatastoreRequestDataAttributes,
        )
        from datadog_api_client.v2.model.update_apps_datastore_request_data_type import (
            UpdateAppsDatastoreRequestDataType,
        )

        return {
            "attributes": (UpdateAppsDatastoreRequestDataAttributes,),
            "id": (str,),
            "type": (UpdateAppsDatastoreRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: UpdateAppsDatastoreRequestDataType,
        attributes: Union[UpdateAppsDatastoreRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``UpdateAppsDatastoreRequestData`` object.

        :param attributes: The definition of ``UpdateAppsDatastoreRequestDataAttributes`` object.
        :type attributes: UpdateAppsDatastoreRequestDataAttributes, optional

        :param id: The ``UpdateAppsDatastoreRequestData`` ``id``.
        :type id: str, optional

        :param type: Datastores resource type.
        :type type: UpdateAppsDatastoreRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
