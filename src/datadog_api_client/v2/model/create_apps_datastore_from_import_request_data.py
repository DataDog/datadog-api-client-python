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
    from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data_attributes import (
        CreateAppsDatastoreFromImportRequestDataAttributes,
    )
    from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data_type import (
        CreateAppsDatastoreFromImportRequestDataType,
    )


class CreateAppsDatastoreFromImportRequestData(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data_attributes import (
            CreateAppsDatastoreFromImportRequestDataAttributes,
        )
        from datadog_api_client.v2.model.create_apps_datastore_from_import_request_data_type import (
            CreateAppsDatastoreFromImportRequestDataType,
        )

        return {
            "attributes": (CreateAppsDatastoreFromImportRequestDataAttributes,),
            "id": (str,),
            "type": (CreateAppsDatastoreFromImportRequestDataType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(
        self_,
        type: CreateAppsDatastoreFromImportRequestDataType,
        attributes: Union[CreateAppsDatastoreFromImportRequestDataAttributes, UnsetType] = unset,
        id: Union[str, UnsetType] = unset,
        **kwargs,
    ):
        """
        The definition of ``CreateAppsDatastoreFromImportRequestData`` object.

        :param attributes: The definition of ``CreateAppsDatastoreFromImportRequestDataAttributes`` object.
        :type attributes: CreateAppsDatastoreFromImportRequestDataAttributes, optional

        :param id: The ``CreateAppsDatastoreFromImportRequestData`` ``id``.
        :type id: str, optional

        :param type: Datastores resource type.
        :type type: CreateAppsDatastoreFromImportRequestDataType
        """
        if attributes is not unset:
            kwargs["attributes"] = attributes
        if id is not unset:
            kwargs["id"] = id
        super().__init__(kwargs)

        self_.type = type
