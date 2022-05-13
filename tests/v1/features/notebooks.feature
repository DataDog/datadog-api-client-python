@endpoint(notebooks) @endpoint(notebooks-v1)
Feature: Notebooks
  Interact with your notebooks through the API to make it easier to
  organize, find, and share all of your notebooks with your team and
  organization. For more information, see the [Notebooks
  documentation](https://docs.datadoghq.com/notebooks/).

  Background:
    Given a valid "apiKeyAuth" key in the system
    And a valid "appKeyAuth" key in the system
    And an instance of "Notebooks" API

  @generated @skip @team:DataDog/notebooks
  Scenario: Create a notebook returns "Bad Request" response
    Given new "CreateNotebook" request
    And body with value {"data": {"attributes": {"cells": [{"attributes": {"definition": {"text": "## Some test markdown\n\n```js\nvar x, y;\nx = 5;\ny = 6;\n```", "type": "markdown"}}, "type": "notebook_cells"}, {"attributes": {"definition": {"requests": [{"display_type": "line", "q": "avg:system.load.1{*}", "style": {"line_type": "solid", "line_width": "normal", "palette": "dog_classic"}}], "show_legend": true, "type": "timeseries", "yaxis": {"scale": "linear"}}, "graph_size": "m", "split_by": {"keys": [], "tags": []}, "time": null}, "type": "notebook_cells"}], "metadata": {"is_template": false, "take_snapshots": false, "type": "investigation"}, "name": "Example Notebook", "status": "published", "time": {"live_span": "1h"}}, "type": "notebooks"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/notebooks
  Scenario: Create a notebook returns "OK" response
    Given new "CreateNotebook" request
    And body with value {"data": {"attributes": {"cells": [{"attributes": {"definition": {"text": "## Some test markdown\n\n```js\nvar x, y;\nx = 5;\ny = 6;\n```", "type": "markdown"}}, "type": "notebook_cells"}, {"attributes": {"definition": {"requests": [{"display_type": "line", "q": "avg:system.load.1{*}", "style": {"line_type": "solid", "line_width": "normal", "palette": "dog_classic"}}], "show_legend": true, "type": "timeseries", "yaxis": {"scale": "linear"}}, "graph_size": "m", "split_by": {"keys": [], "tags": []}, "time": null}, "type": "notebook_cells"}], "name": "{{ unique }}", "status": "published", "time": {"live_span": "1h"}}, "type": "notebooks"}}
    When the request is sent
    Then the response status is 200 OK

  @skip @team:DataDog/notebooks
  Scenario: Delete a notebook returns "Bad Request" response
    Given new "DeleteNotebook" request
    And request contains "notebook_id" parameter with value "ThisIsntANotebookId"
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/notebooks
  Scenario: Delete a notebook returns "Not Found" response
    Given new "DeleteNotebook" request
    And request contains "notebook_id" parameter with value 123456
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/notebooks
  Scenario: Delete a notebook returns "OK" response
    Given new "DeleteNotebook" request
    And there is a valid "notebook" in the system
    And request contains "notebook_id" parameter from "notebook.data.id"
    When the request is sent
    Then the response status is 204 OK

  @generated @skip @team:DataDog/notebooks
  Scenario: Get a notebook returns "Bad Request" response
    Given new "GetNotebook" request
    And request contains "notebook_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/notebooks
  Scenario: Get a notebook returns "Not Found" response
    Given new "GetNotebook" request
    And request contains "notebook_id" parameter from "REPLACE.ME"
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/notebooks
  Scenario: Get a notebook returns "OK" response
    Given new "GetNotebook" request
    And there is a valid "notebook" in the system
    And request contains "notebook_id" parameter from "notebook.data.id"
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/notebooks
  Scenario: Get all notebooks returns "Bad Request" response
    Given new "ListNotebooks" request
    When the request is sent
    Then the response status is 400 Bad Request

  @team:DataDog/notebooks
  Scenario: Get all notebooks returns "OK" response
    Given new "ListNotebooks" request
    When the request is sent
    Then the response status is 200 OK

  @generated @skip @team:DataDog/notebooks
  Scenario: Update a notebook returns "Bad Request" response
    Given new "UpdateNotebook" request
    And request contains "notebook_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cells": [{"attributes": {"definition": {"text": "## Some test markdown\n\n```js\nvar x, y;\nx = 5;\ny = 6;\n```", "type": "markdown"}}, "id": "bzbycoya", "type": "notebook_cells"}, {"attributes": {"definition": {"requests": [{"display_type": "line", "q": "avg:system.load.1{*}", "style": {"line_type": "solid", "line_width": "normal", "palette": "dog_classic"}}], "show_legend": true, "type": "timeseries", "yaxis": {"scale": "linear"}}, "graph_size": "m", "split_by": {"keys": [], "tags": []}, "time": null}, "id": "9k6bc6xc", "type": "notebook_cells"}], "metadata": {"is_template": false, "take_snapshots": false, "type": "investigation"}, "name": "Example Notebook", "status": "published", "time": {"live_span": "1h"}}, "type": "notebooks"}}
    When the request is sent
    Then the response status is 400 Bad Request

  @generated @skip @team:DataDog/notebooks
  Scenario: Update a notebook returns "Conflict" response
    Given new "UpdateNotebook" request
    And request contains "notebook_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cells": [{"attributes": {"definition": {"text": "## Some test markdown\n\n```js\nvar x, y;\nx = 5;\ny = 6;\n```", "type": "markdown"}}, "id": "bzbycoya", "type": "notebook_cells"}, {"attributes": {"definition": {"requests": [{"display_type": "line", "q": "avg:system.load.1{*}", "style": {"line_type": "solid", "line_width": "normal", "palette": "dog_classic"}}], "show_legend": true, "type": "timeseries", "yaxis": {"scale": "linear"}}, "graph_size": "m", "split_by": {"keys": [], "tags": []}, "time": null}, "id": "9k6bc6xc", "type": "notebook_cells"}], "metadata": {"is_template": false, "take_snapshots": false, "type": "investigation"}, "name": "Example Notebook", "status": "published", "time": {"live_span": "1h"}}, "type": "notebooks"}}
    When the request is sent
    Then the response status is 409 Conflict

  @generated @skip @team:DataDog/notebooks
  Scenario: Update a notebook returns "Not Found" response
    Given new "UpdateNotebook" request
    And request contains "notebook_id" parameter from "REPLACE.ME"
    And body with value {"data": {"attributes": {"cells": [{"attributes": {"definition": {"text": "## Some test markdown\n\n```js\nvar x, y;\nx = 5;\ny = 6;\n```", "type": "markdown"}}, "id": "bzbycoya", "type": "notebook_cells"}, {"attributes": {"definition": {"requests": [{"display_type": "line", "q": "avg:system.load.1{*}", "style": {"line_type": "solid", "line_width": "normal", "palette": "dog_classic"}}], "show_legend": true, "type": "timeseries", "yaxis": {"scale": "linear"}}, "graph_size": "m", "split_by": {"keys": [], "tags": []}, "time": null}, "id": "9k6bc6xc", "type": "notebook_cells"}], "metadata": {"is_template": false, "take_snapshots": false, "type": "investigation"}, "name": "Example Notebook", "status": "published", "time": {"live_span": "1h"}}, "type": "notebooks"}}
    When the request is sent
    Then the response status is 404 Not Found

  @team:DataDog/notebooks
  Scenario: Update a notebook returns "OK" response
    Given new "UpdateNotebook" request
    And there is a valid "notebook" in the system
    And request contains "notebook_id" parameter from "notebook.data.id"
    And body with value {"data": {"attributes": {"cells": [{"attributes": {"definition": {"text": "## Some test markdown\n\n```js\nvar x, y;\nx = 5;\ny = 6;\n```", "type": "markdown"}}, "type": "notebook_cells"}, {"attributes": {"definition": {"requests": [{"display_type": "line", "q": "avg:system.load.1{*}", "style": {"line_type": "solid", "line_width": "normal", "palette": "dog_classic"}}], "show_legend": true, "type": "timeseries", "yaxis": {"scale": "linear"}}, "graph_size": "m", "split_by": {"keys": [], "tags": []}, "time": null}, "type": "notebook_cells"}], "name": "{{ unique }}-updated", "status": "published", "time": {"live_span": "1h"}}, "type": "notebooks"}}
    When the request is sent
    Then the response status is 200 OK
