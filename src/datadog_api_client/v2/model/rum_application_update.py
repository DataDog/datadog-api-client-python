# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class RUMApplicationUpdate(ModelNormal):
    @cached_property
    def openapi_types(_):
        from datadog_api_client.v2.model.rum_application_update_attributes import RUMApplicationUpdateAttributes
        from datadog_api_client.v2.model.rum_application_update_type import RUMApplicationUpdateType

        return {
            "attributes": (RUMApplicationUpdateAttributes,),
            "id": (str,),
            "type": (RUMApplicationUpdateType,),
        }

    attribute_map = {
        "attributes": "attributes",
        "id": "id",
        "type": "type",
    }

    def __init__(self_, id, type, *args, **kwargs):
        """
        RUM application update.

        :param attributes: RUM application update attributes.
        :type attributes: RUMApplicationUpdateAttributes, optional

        :param id: RUM application ID.
        :type id: str

        :param type: RUM application update type.
        :type type: RUMApplicationUpdateType
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.id = id
        self_.type = type
