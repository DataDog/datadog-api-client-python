import os
from dateutil.parser import parse as dateutil_parser
from datadog_api_client.v1 import ApiClient, ApiException, Configuration
from datadog_api_client.v1.api import notebooks_api
from datadog_api_client.v1.models import *
from pprint import pprint
# See configuration.py for a list of all supported configuration parameters.
configuration = Configuration()

# Enter a context with an instance of the API client
with ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = notebooks_api.NotebooksApi(api_client)
    body = NotebookCreateRequest(
        data=NotebookCreateData(
            attributes=NotebookCreateDataAttributes(
                cells=[
                    NotebookCellCreateRequest(
                        attributes=NotebookCellCreateRequestAttributes(),
                        type=NotebookCellResourceType("notebook_cells"),
                    ),
                ],
                metadata=NotebookMetadata(
                    is_template=False,
                    take_snapshots=False,
                    type=NotebookMetadataType("investigation"),
                ),
                name="Example Notebook",
                status=NotebookStatus("published"),
                time=NotebookGlobalTime(),
            ),
            type=NotebookResourceType("notebooks"),
        ),
    )  # NotebookCreateRequest | The JSON description of the notebook you want to create.

    # example passing only required values which don't have defaults set
    try:
        # Create a notebook
        api_response = api_instance.create_notebook(body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NotebooksApi->create_notebook: %s\n" % e)
