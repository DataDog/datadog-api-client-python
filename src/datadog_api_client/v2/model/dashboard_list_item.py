# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
    datetime,
)


class DashboardListItem(ModelNormal):
    validations = {
        "popularity": {
            "inclusive_maximum": 5,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.creator import Creator
        from datadog_api_client.v2.model.dashboard_type import DashboardType

        return {
            "author": (Creator,),
            "created": (datetime,),
            "icon": (str,),
            "id": (str,),
            "is_favorite": (bool,),
            "is_read_only": (bool,),
            "is_shared": (bool,),
            "modified": (datetime,),
            "popularity": (int,),
            "title": (str,),
            "type": (DashboardType,),
            "url": (str,),
        }

    attribute_map = {
        "author": "author",
        "created": "created",
        "icon": "icon",
        "id": "id",
        "is_favorite": "is_favorite",
        "is_read_only": "is_read_only",
        "is_shared": "is_shared",
        "modified": "modified",
        "popularity": "popularity",
        "title": "title",
        "type": "type",
        "url": "url",
    }
    read_only_vars = {
        "created",
        "icon",
        "is_favorite",
        "is_read_only",
        "is_shared",
        "modified",
        "popularity",
        "title",
        "url",
    }

    def __init__(self, id, type, *args, **kwargs):
        """
        A dashboard within a list.

        :param author: Creator of the object.
        :type author: Creator, optional

        :param created: Date of creation of the dashboard.
        :type created: datetime, optional

        :param icon: URL to the icon of the dashboard.
        :type icon: str, optional

        :param id: ID of the dashboard.
        :type id: str

        :param is_favorite: Whether or not the dashboard is in the favorites.
        :type is_favorite: bool, optional

        :param is_read_only: Whether or not the dashboard is read only.
        :type is_read_only: bool, optional

        :param is_shared: Whether the dashboard is publicly shared or not.
        :type is_shared: bool, optional

        :param modified: Date of last edition of the dashboard.
        :type modified: datetime, optional

        :param popularity: Popularity of the dashboard.
        :type popularity: int, optional

        :param title: Title of the dashboard.
        :type title: str, optional

        :param type: The type of the dashboard.
        :type type: DashboardType

        :param url: URL path to the dashboard.
        :type url: str, optional
        """
        super().__init__(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type

    @classmethod
    def _from_openapi_data(cls, id, type, *args, **kwargs):
        """Helper creating a new instance from a response."""

        self = super(DashboardListItem, cls)._from_openapi_data(kwargs)

        self._check_pos_args(args)

        self.id = id
        self.type = type
        return self
