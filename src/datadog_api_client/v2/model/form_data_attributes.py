# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.
from __future__ import annotations

from typing import Union, TYPE_CHECKING

from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
    unset,
    UnsetType,
    UUID,
)


if TYPE_CHECKING:
    from datadog_api_client.v2.model.form_datastore_config_attributes import FormDatastoreConfigAttributes
    from datadog_api_client.v2.model.form_publication_attributes import FormPublicationAttributes
    from datadog_api_client.v2.model.form_version_attributes import FormVersionAttributes


class FormDataAttributes(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.form_datastore_config_attributes import FormDatastoreConfigAttributes
        from datadog_api_client.v2.model.form_publication_attributes import FormPublicationAttributes
        from datadog_api_client.v2.model.form_version_attributes import FormVersionAttributes

        return {
            "active": (bool,),
            "anonymous": (bool,),
            "created_at": (datetime,),
            "datastore_config": (FormDatastoreConfigAttributes,),
            "description": (str,),
            "end_date": (datetime, none_type),
            "has_submitted": (bool, none_type),
            "idp_survey": (bool,),
            "modified_at": (datetime,),
            "name": (str,),
            "org_id": (int,),
            "publication": (FormPublicationAttributes,),
            "self_service": (bool,),
            "single_response": (bool,),
            "user_id": (int,),
            "user_uuid": (UUID,),
            "version": (FormVersionAttributes,),
        }

    attribute_map = {
        "active": "active",
        "anonymous": "anonymous",
        "created_at": "created_at",
        "datastore_config": "datastore_config",
        "description": "description",
        "end_date": "end_date",
        "has_submitted": "has_submitted",
        "idp_survey": "idp_survey",
        "modified_at": "modified_at",
        "name": "name",
        "org_id": "org_id",
        "publication": "publication",
        "self_service": "self_service",
        "single_response": "single_response",
        "user_id": "user_id",
        "user_uuid": "user_uuid",
        "version": "version",
    }

    def __init__(
        self_,
        active: bool,
        anonymous: bool,
        created_at: datetime,
        datastore_config: FormDatastoreConfigAttributes,
        description: str,
        idp_survey: bool,
        modified_at: datetime,
        name: str,
        org_id: int,
        self_service: bool,
        single_response: bool,
        user_id: int,
        user_uuid: UUID,
        end_date: Union[datetime, none_type, UnsetType] = unset,
        has_submitted: Union[bool, none_type, UnsetType] = unset,
        publication: Union[FormPublicationAttributes, UnsetType] = unset,
        version: Union[FormVersionAttributes, UnsetType] = unset,
        **kwargs,
    ):
        """
        The attributes of a form.

        :param active: Whether the form is currently active.
        :type active: bool

        :param anonymous: Whether the form accepts anonymous submissions.
        :type anonymous: bool

        :param created_at: The time at which the form was created.
        :type created_at: datetime

        :param datastore_config: The datastore configuration for a form.
        :type datastore_config: FormDatastoreConfigAttributes

        :param description: The description of the form.
        :type description: str

        :param end_date: The date and time at which the form stops accepting responses.
        :type end_date: datetime, none_type, optional

        :param has_submitted: Whether the current user has already submitted this form. Only present for forms with
            ``single_response`` set to ``true``.
        :type has_submitted: bool, none_type, optional

        :param idp_survey: Whether the form is an IDP survey.
        :type idp_survey: bool

        :param modified_at: The time at which the form was last modified.
        :type modified_at: datetime

        :param name: The name of the form.
        :type name: str

        :param org_id: The ID of the organization that owns this form.
        :type org_id: int

        :param publication: The attributes of a form publication.
        :type publication: FormPublicationAttributes, optional

        :param self_service: Whether the form is available in the self-service catalog.
        :type self_service: bool

        :param single_response: Whether each user can only submit one response.
        :type single_response: bool

        :param user_id: The ID of the user who created this form.
        :type user_id: int

        :param user_uuid: The UUID of the user who created this form.
        :type user_uuid: UUID

        :param version: The attributes of a form version.
        :type version: FormVersionAttributes, optional
        """
        if end_date is not unset:
            kwargs["end_date"] = end_date
        if has_submitted is not unset:
            kwargs["has_submitted"] = has_submitted
        if publication is not unset:
            kwargs["publication"] = publication
        if version is not unset:
            kwargs["version"] = version
        super().__init__(kwargs)

        self_.active = active
        self_.anonymous = anonymous
        self_.created_at = created_at
        self_.datastore_config = datastore_config
        self_.description = description
        self_.idp_survey = idp_survey
        self_.modified_at = modified_at
        self_.name = name
        self_.org_id = org_id
        self_.self_service = self_service
        self_.single_response = single_response
        self_.user_id = user_id
        self_.user_uuid = user_uuid
