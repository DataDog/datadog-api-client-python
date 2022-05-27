# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
    none_type,
)


class DashboardSummaryDefinition(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.dashboard_layout_type import DashboardLayoutType

        return {
            "author_handle": (str,),
            "created_at": (datetime,),
            "description": (str, none_type),
            "id": (str,),
            "is_read_only": (bool,),
            "layout_type": (DashboardLayoutType,),
            "modified_at": (datetime,),
            "title": (str,),
            "url": (str,),
        }

    attribute_map = {
        "author_handle": "author_handle",
        "created_at": "created_at",
        "description": "description",
        "id": "id",
        "is_read_only": "is_read_only",
        "layout_type": "layout_type",
        "modified_at": "modified_at",
        "title": "title",
        "url": "url",
    }

    def __init__(self, *args, **kwargs):
        """
        Dashboard definition.

        :param author_handle: Identifier of the dashboard author.
        :type author_handle: str, optional

        :param created_at: Creation date of the dashboard.
        :type created_at: datetime, optional

        :param description: Description of the dashboard.
        :type description: str, none_type, optional

        :param id: Dashboard identifier.
        :type id: str, optional

        :param is_read_only: Whether this dashboard is read-only. If True, only the author and admins can make changes to it.
        :type is_read_only: bool, optional

        :param layout_type: Layout type of the dashboard.
        :type layout_type: DashboardLayoutType, optional

        :param modified_at: Modification date of the dashboard.
        :type modified_at: datetime, optional

        :param title: Title of the dashboard.
        :type title: str, optional

        :param url: URL of the dashboard.
        :type url: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

    @classmethod
    def _from_openapi_data(cls, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardSummaryDefinition, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        return self
