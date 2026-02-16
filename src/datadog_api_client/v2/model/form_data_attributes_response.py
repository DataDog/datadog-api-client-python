# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.form_datastore_config import FormDatastoreConfig
    from datadog_api_client.v2.model.form_publication import FormPublication
    from datadog_api_client.v2.model.form_version import FormVersion


class FormDataAttributesResponse(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_datastore_config import FormDatastoreConfig
        from datadog_api_client.v2.model.form_publication import FormPublication
        from datadog_api_client.v2.model.form_version import FormVersion

        return {
            "created_at": (datetime,),
            "datastore_config": (FormDatastoreConfig,),
            "description": (str,),
            "modified_at": (datetime,),
            "name": (str,),
            "org_id": (int,),
            "publication": (FormPublication,),
            "user_id": (int,),
            "user_uuid": (UUID,),
            "version": (FormVersion,),
        }

    attribute_map = {
        "created_at": "created_at",
        "datastore_config": "datastore_config",
        "description": "description",
        "modified_at": "modified_at",
        "name": "name",
        "org_id": "org_id",
        "publication": "publication",
        "user_id": "user_id",
        "user_uuid": "user_uuid",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        datastore_config: FormDatastoreConfig,
        description: str,
        modified_at: datetime,
        name: str,
        org_id: int,
        user_id: int,
        user_uuid: UUID,
        publication: Union[FormPublication, UnsetType] = unset,
        version: Union[FormVersion, UnsetType] = unset,
        **kwargs,
    ):
        """
        Attributes of a form.

        :param created_at: Creation timestamp.
        :type created_at: datetime

        :param datastore_config: Configuration for the form's associated datastore.
        :type datastore_config: FormDatastoreConfig

        :param description: The description of the form.
        :type description: str

        :param modified_at: Last modification timestamp.
        :type modified_at: datetime

        :param name: The name of the form.
        :type name: str

        :param org_id: The organization ID.
        :type org_id: int

        :param publication: Publication information for the form.
        :type publication: FormPublication, optional

        :param user_id: The ID of the user who created the form.
        :type user_id: int

        :param user_uuid: The UUID of the user who created the form.
        :type user_uuid: UUID

        :param version: Version information for the form.
        :type version: FormVersion, optional
        """
        if publication is not unset:
            kwargs["publication"] = publication
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.datastore_config = datastore_config
        self_.description = description
        self_.modified_at = modified_at
        self_.name = name
        self_.org_id = org_id
        self_.user_id = user_id
        self_.user_uuid = user_uuid
