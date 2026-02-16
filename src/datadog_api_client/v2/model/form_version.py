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
    from datadog_api_client.v2.model.form_version_state import FormVersionState


class FormVersion(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_version_state import FormVersionState

        return {
            "created_at": (datetime,),
            "data_definition": (dict,),
            "definition_signature": (str,),
            "etag": (str,),
            "id": (str,),
            "modified_at": (datetime,),
            "state": (FormVersionState,),
            "ui_definition": (dict,),
            "user_id": (int,),
            "user_uuid": (UUID,),
            "version": (int,),
        }

    attribute_map = {
        "created_at": "created_at",
        "data_definition": "data_definition",
        "definition_signature": "definition_signature",
        "etag": "etag",
        "id": "id",
        "modified_at": "modified_at",
        "state": "state",
        "ui_definition": "ui_definition",
        "user_id": "user_id",
        "user_uuid": "user_uuid",
        "version": "version",
    }

    def __init__(
        self_,
        created_at: datetime,
        data_definition: dict,
        id: str,
        modified_at: datetime,
        state: FormVersionState,
        ui_definition: dict,
        user_id: int,
        user_uuid: UUID,
        definition_signature: Union[str, UnsetType] = unset,
        etag: Union[str, UnsetType] = unset,
        version: Union[int, UnsetType] = unset,
        **kwargs,
    ):
        """
        Version information for the form.

        :param created_at: Creation timestamp.
        :type created_at: datetime

        :param data_definition: The data definition for the form.
        :type data_definition: dict

        :param definition_signature: Signature of the form definition.
        :type definition_signature: str, optional

        :param etag: The entity tag for the version.
        :type etag: str, optional

        :param id: The unique identifier of the form version.
        :type id: str

        :param modified_at: Last modification timestamp.
        :type modified_at: datetime

        :param state: The state of the form version.
        :type state: FormVersionState

        :param ui_definition: The UI definition for the form.
        :type ui_definition: dict

        :param user_id: The ID of the user who created the version.
        :type user_id: int

        :param user_uuid: The UUID of the user who created the version.
        :type user_uuid: UUID

        :param version: The version number.
        :type version: int, optional
        """
        if definition_signature is not unset:
            kwargs["definition_signature"] = definition_signature
        if etag is not unset:
            kwargs["etag"] = etag
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.created_at = created_at
        self_.data_definition = data_definition
        self_.id = id
        self_.modified_at = modified_at
        self_.state = state
        self_.ui_definition = ui_definition
        self_.user_id = user_id
        self_.user_uuid = user_uuid
