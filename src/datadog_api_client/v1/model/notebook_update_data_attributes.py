# Unless explicitly stated otherwise all files in this repository are licensed under the Apache-2.0 License.
# This product includes software developed at Datadog (https://www.datadoghq.com/).
# Copyright 2019-Present Datadog, Inc.


from datadog_api_client.model_utils import (
    ModelNormal,
    cached_property,
)


class NotebookUpdateDataAttributes(ModelNormal):
    validations = {
        "name": {
            "max_length": 80,
            "min_length": 0,
        },
    }

    @cached_property
    def openapi_types(_):
        from datadog_api_client.v1.model.notebook_update_cell import NotebookUpdateCell
        from datadog_api_client.v1.model.notebook_metadata import NotebookMetadata
        from datadog_api_client.v1.model.notebook_status import NotebookStatus
        from datadog_api_client.v1.model.notebook_global_time import NotebookGlobalTime

        return {
            "cells": ([NotebookUpdateCell],),
            "metadata": (NotebookMetadata,),
            "name": (str,),
            "status": (NotebookStatus,),
            "time": (NotebookGlobalTime,),
        }

    attribute_map = {
        "cells": "cells",
        "metadata": "metadata",
        "name": "name",
        "status": "status",
        "time": "time",
    }

    def __init__(self_, cells, name, time, *args, **kwargs):
        """
        The data attributes of a notebook.

        :param cells: List of cells to display in the notebook.
        :type cells: [NotebookUpdateCell]

        :param metadata: Metadata associated with the notebook.
        :type metadata: NotebookMetadata, optional

        :param name: The name of the notebook.
        :type name: str

        :param status: Publication status of the notebook. For now, always "published".
        :type status: NotebookStatus, optional

        :param time: Notebook global timeframe.
        :type time: NotebookGlobalTime
        """
        super().__init__(kwargs)

        self_._check_pos_args(args)

        self_.cells = cells
        self_.name = name
        self_.time = time
